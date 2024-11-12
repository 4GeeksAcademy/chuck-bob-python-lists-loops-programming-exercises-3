parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here



def get_parking_lot(parking_state):
  parking_dict = {
    "total_slots" : 0,
    "available_slots" : 0,
    "occupied_slots" : 0
  }

  for i in parking_state:
      for x in i:
          if x == 1:
              parking_dict["occupied_slots"] += 1
          if x == 2:
              parking_dict["available_slots"] += 1 
  parking_dict["total_slots"] = parking_dict["occupied_slots"] + parking_dict["available_slots"]
  return parking_dict
    
result = get_parking_lot(parking_state)

print(result)

