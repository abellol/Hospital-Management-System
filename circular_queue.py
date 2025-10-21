from doctors import Doctor
class CircularQueue:
  """
  CircularQueue manages a fixed-size rotation of doctors in a hospital or clinic.
  
  This structure ensures that all available doctors take turns attending patients
  in a fair and continuous order. When the end of the list is reached, the queue
  automatically cycles back to the first doctor, creating an infinite rotation loop.
  """

  def __init__(self, capacity):
    """
    Initialize the circular queue with a defined maximum number of doctors.

    Args:
      capacity (int): The maximum number of doctors that can be registered
        in the rotation at a given time.
    """
    self.capacity = capacity
    self.queue = [None] * capacity
    self.front = 0
    self.rear = -1
    self.size = 0

  def is_empty(self):
    """
    Check if there are no doctors currently registered in the rotation.

    Returns:
      bool: True if no doctors are in the queue, False otherwise.
    """
    return self.size == 0

  def is_full(self):
    """
    Check if the doctor rotation list has reached its maximum capacity.

    Returns:
      bool: True if the queue is full, False otherwise.
    """
    return self.size == self.capacity

  def add_doctor(self, doctor:Doctor):
    """
    Add a doctor to the rotation schedule. If the queue is full,
    the doctor cannot be added until a slot is freed.

    Args:
      doctor (Doctor): The doctor object to register in the rotation.
    """
    if self.is_full():
      print("Cannot add more doctors: rotation list is full.")
      return
    self.rear = (self.rear + 1) % self.capacity
    self.queue[self.rear] = doctor
    self.size += 1
    print(f"Doctor {doctor.name} added to the rotation.")

  def next_doctor(self):
    """
    Retrieve the next doctor in the rotation, moving the front pointer forward.
    Once the end of the queue is reached, it restarts from the beginning.

    Returns:
      Doctor or None: The next doctor scheduled for duty,
      or None if no doctors are available.
    """
    if self.is_empty():
      print("No doctors available for rotation.")
      return None
    doctor = self.queue[self.front]
    self.front = (self.front + 1) % self.capacity
    return doctor

  def show_doctors(self):
    """
    Display the list of doctors currently active in the rotation,
    starting from the current front position.

    Prints:
      A formatted list showing the rotation order of all registered doctors.
    """
    if self.is_empty():
      print("No doctors currently registered in the rotation.")
      return
  
    print("Current doctor rotation order:")
    i = self.front
    count = 0
  
    while count < self.size:
      doctor = self.queue[i]
      if doctor is not None:
        print(" ->", doctor.show_info())
      i = (i + 1) % self.capacity
      count += 1