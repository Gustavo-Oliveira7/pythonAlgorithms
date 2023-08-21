def study_schedule(permanence_period, target_time):
    count = 0
    for i in permanence_period:
        try:
            if i[0] <= target_time <= i[1]:
                count += 1
        except:
            return None
    return count
