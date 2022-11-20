#  check if already in position
def already_in_position(positions,symbol,final_signal):
    if len(positions["netPositions"]) == 0: return False
    for position in positions["netPositions"]:
        pos_symbol = position["symbol"]  # NSE:SBIN-EQ
        side =  position["side"]  # 1 for long, -1 for short, and 0 for closed

        if pos_symbol == symbol and side == final_signal:
            return True
        else:
            return False
    

#  check if done for the day or not
def check_three_loses(positions):
    if len(positions["netPositions"]) == 0: return False
    for position in positions["netPositions"]:
        count = 0
        if position["side"] == 0:
            if position["pl"] < 0:
                count= count+1
    return count>=3