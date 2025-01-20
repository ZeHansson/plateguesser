def readfile(path_to_data):
    with open(path_to_data) as f:
        file_contents = f.read()
    return file_contents

def calc_avg(data):
    listed_data = data.split()

    #Split data into days
    mon_val = listed_data[7:-4:6]
    tue_val = listed_data[8:-3:6]
    wed_val = listed_data[9:-2:6]
    thu_val = listed_data[10:-1:6]
    fri_val = listed_data[11::6]

    mon_avg = 0
    tue_avg = 0
    wed_avg = 0
    thu_avg = 0
    fri_avg = 0

    for i in range(0, len(mon_val)):
        mon_avg += int(mon_val[i].split("-")[0])
        tue_avg += int(tue_val[i].split("-")[0])
        wed_avg += int(wed_val[i].split("-")[0])
        thu_avg += int(thu_val[i].split("-")[0])
        fri_avg += int(fri_val[i].split("-")[0])

    mon_state = "j" in mon_val[len(mon_val)-1]
    tue_state = "j" in tue_val[len(tue_val)-1]
    wed_state = "j" in wed_val[len(wed_val)-1]
    thu_state = "j" in thu_val[len(thu_val)-1]
    fri_state = "j" in fri_val[len(fri_val)-1]
     
    mon_avg = mon_avg/len(mon_val)
    tue_avg = tue_avg/len(tue_val)
    wed_avg = wed_avg/len(wed_val)
    thu_avg = thu_avg/len(thu_val)
    fri_avg = fri_avg/len(fri_val)
    
    return mon_avg, mon_state, tue_avg, tue_state, wed_avg, wed_state, thu_avg, thu_state, fri_avg, fri_state

def make_rep(mon,mon_state, tue, tue_state,wed, wed_state,thu, thu_state,fri, fri_state):
    print("Average plates for days & if there where enough (last week only) :")
    print("___________________________________________________")
    print(f"Average is {mon} & Was there enough? : {mon_state}")
    print(f"Average is {tue} & Was there enough? : {tue_state}")
    print(f"Average is {wed} & Was there enough? : {wed_state}")
    print(f"Average is {thu} & Was there enough? : {thu_state}")
    print(f"Average is {fri} & Was there enough? : {fri_state}")
    print("___________________________________________________")
    print("Thanks for your attention, have a great day.")


if __name__ == '__main__':
    path = "data.txt"
    data = readfile(path)
    #print(calc_avg(data))
    results = calc_avg(data)
    make_rep(results[0],results[1],results[2],results[3],results[4],results[5],results[6],results[7],results[8],results[9])



    #print(data)