import csv
import os


def datapoint(num):
    with open((str(num) + '.csv'), 'r') as f:
      reader = csv.reader(f)
      your_list = list(reader)

    return your_list

def alldrawingdsdata():
    with open(('data.txt'), 'r') as f:
      reader = csv.reader(f)
      your_list = list(reader)

    return your_list


def parse_directions():
    direction_data = {}

    for d in range(1, 44):
        data = datapoint(d)
        right = 0
        up = 0
        left = 0
        down = 0
        for i in range(1, len(data)):
            if (data[i][0] == 'right'):
                right += 1
            if (data[i][0] == 'up'):
                up += 1
            if (data[i][0] == 'left'):
                left += 1
            if (data[i][0] == 'down'):
                down += 1
        direction_data[d] = {"right": right, "up": up, "left": left, "down": down}
    print_direction_data(direction_data)

def print_direction_data(direction_data):

    with open('output/directiondata.csv', 'a') as the_file:
        the_file.write("participant, right, up, left, down\n")
        for d in range(1,44):
            the_file.write(str(d) + ", " + str(direction_data[d]["right"]) + ", " + str(direction_data[d]["up"]) + ", " + str(direction_data[d]["left"]) + ", " + str(direction_data[d]["down"]) + "\n")


def parse_slide_type_visited():
    slide_type_data = {}

    for d in range(1, 44):
        data = datapoint(d)
        v = 0
        t = 0
        b = 0
        p = 0
        for i in range(1, len(data)):
            if (data[i][2] == ' v'):
                v += 1
            if (data[i][2] == ' t'):
                t += 1
            if (data[i][2] == ' b'):
                b += 1
            if (data[i][2] == ' p'):
                p += 1
        slide_type_data[d] = {"v": v, "t": t, "b": b, "p": p}
    print_slide_type_data(slide_type_data)

def print_slide_type_data(slide_type_data):

    with open('output/slidetypedata.csv', 'a') as the_file:
        the_file.write("participant, v, t, b, p\n")
        for d in range(1,44):
            the_file.write(str(d) + ", " + str(slide_type_data[d]["v"]) + ", " + str(slide_type_data[d]["t"]) + ", " + str(slide_type_data[d]["b"]) + ", " + str(slide_type_data[d]["p"]) + "\n")


def parse_next_directions():
    next_directions = {}

    for d in range(1, 44):
        data = datapoint(d)
        current_v = {"v": 0, "t": 0, "b": 0, "p": 0}
        current_t = {"v": 0, "t": 0, "b": 0, "p": 0}
        current_b = {"v": 0, "t": 0, "b": 0, "p": 0}
        current_p = {"v": 0, "t": 0, "b": 0, "p": 0}
        for i in range(2, len(data)):
            if (data[i][2] == ' v'):
                if (data[i-1][2] == ' v'):
                    current_v["v"] += 1
                if (data[i-1][2] == ' t'):
                    current_t["v"] += 1
                if (data[i-1][2] == ' b'):
                    current_b["v"] += 1
                if (data[i-1][2] == ' p'):
                    current_p["v"] += 1

            if (data[i][2] == ' t'):
                if (data[i-1][2] == ' v'):
                    current_v["t"] += 1
                if (data[i-1][2] == ' t'):
                    current_t["t"] += 1
                if (data[i-1][2] == ' b'):
                    current_b["t"] += 1
                if (data[i-1][2] == ' p'):
                    current_p["t"] += 1
            if (data[i][2] == ' b'):
                if (data[i-1][2] == ' v'):
                    current_v["b"] += 1
                if (data[i-1][2] == ' t'):
                    current_t["b"] += 1
                if (data[i-1][2] == ' b'):
                    current_b["b"] += 1
                if (data[i-1][2] == ' p'):
                    current_p["b"] += 1
            if (data[i][2] == ' p'):
                if (data[i-1][2] == ' v'):
                    current_v["p"] += 1
                if (data[i-1][2] == ' t'):
                    current_t["p"] += 1
                if (data[i-1][2] == ' b'):
                    current_b["p"] += 1
                if (data[i-1][2] == ' p'):
                    current_p["p"] += 1
        next_directions[d] = {"current_v": current_v, "current_t": current_t, "current_b": current_b, "current_p": current_p}

    print_next_directions_data(next_directions)

def print_next_directions_data(next_directions):
    with open('output/nextdirectionsdata.csv', 'a') as the_file:
        the_file.write("participant, current_v_v, current_v_t, current_v_b, current_v_p, current_t_v, current_t_t, current_t_b, current_t_p, current_b_v, current_b_t, current_b_b, current_b_p, current_p_v, current_p_t, current_p_b, current_p_p\n")
        for d in range(1,44):
            the_file.write(str(d) + ", " + 
                str(next_directions[d]["current_v"]["v"]) + ", " + str(next_directions[d]["current_v"]["t"]) + ", " + str(next_directions[d]["current_v"]["b"]) + ", " + str(next_directions[d]["current_v"]["p"]) + ", " +  
                str(next_directions[d]["current_t"]["v"]) + ", " + str(next_directions[d]["current_t"]["t"]) + ", " + str(next_directions[d]["current_t"]["b"]) + ", " + str(next_directions[d]["current_t"]["p"]) + ", " +  
                str(next_directions[d]["current_b"]["v"]) + ", " + str(next_directions[d]["current_b"]["t"]) + ", " + str(next_directions[d]["current_b"]["b"]) + ", " + str(next_directions[d]["current_b"]["p"]) + ", " +  
                str(next_directions[d]["current_p"]["v"]) + ", " + str(next_directions[d]["current_p"]["t"]) + ", " + str(next_directions[d]["current_p"]["b"]) + ", " + str(next_directions[d]["current_p"]["p"]) + "\n")

def parse_average_timing_per_slide_type():
    slide_time_data = {}
    timings_data = {}

    for d in range(1, 44):
        data = datapoint(d)
        v = 0
        vcounter = 0
        t = 0
        tcounter = 0
        b = 0
        bcounter = 0
        p = 0
        pcounter = 0
        for i in range(1, len(data)):
            if (data[i][2] == ' v'):
                v += float(data[i][4].replace(" ", ""))
                vcounter += 1
            if (data[i][2] == ' t'):
                tcounter += 1
                t += float(data[i][4].replace(" ", ""))
            if (data[i][2] == ' b'):
                bcounter += 1
                b += float(data[i][4].replace(" ", ""))
            if (data[i][2] == ' p'):
                pcounter += 1
                p += float(data[i][4].replace(" ", ""))
        timings_data[d] = {"overall": (v+t+b+p)}
        if (vcounter):
            v = (float(v))/vcounter
        if (tcounter):
            t = (float(t))/tcounter
        if (bcounter):
            b = (float(b))/bcounter
        if (pcounter):
            p = (float(p))/pcounter
        slide_time_data[d] = {"vtime": v, "ttime": t, "btime": b, "ptime": p}

    print_overall_time_data(timings_data)    
    print_slide_time_data(slide_time_data)    

def print_slide_time_data(slide_time_data):

    with open('output/slidetimedata.csv', 'a') as the_file:
        the_file.write("participant, vtime, ttime, btime, ptime\n")
        for d in range(1,44):
            the_file.write(str(d) + ", " + str(slide_time_data[d]["vtime"]) + ", " + str(slide_time_data[d]["ttime"]) + ", " + str(slide_time_data[d]["btime"]) + ", " + str(slide_time_data[d]["ptime"]) + "\n")

def print_overall_time_data(timings_data):

    with open('output/slidetimingsdata.csv', 'a') as the_file:
        the_file.write("participant, overall time\n")
        for d in range(1,44):
            the_file.write(str(d) + ", " + str(timings_data[d]["overall"]) + "\n")

def calculate_node(num, typ):
    if (typ == "v"):
        return str((num-1)*4)
    if (typ == "t"):
        return str(((num-1)*4)+1)
    if (typ == "b"):
        return str(((num-1)*4)+2)
    if (typ == "p"):
        return str(((num-1)*4)+3)


def drawdatapoint(num):
    data = datapoint(num)
    for i in range(1, len(data)-1):
        # print "{source: nodes[" + calculate_node(int(data[i][1].replace(" ", "")[0]), data[i][2].replace(" ", "")[0]) + "], target: nodes[" + calculate_node(int(data[i+1][1].replace(" ", "")[0]), data[i+1][2].replace(" ", "")[0]) +"]},"
        print data[i][1].replace(" ", "")[0] + data[i][2].replace(" ", "")[0] + " to " + data[i+1][1].replace(" ", "")[0] + data[i+1][2].replace(" ", "")[0]
def all_drawings():
    for d in range(1, 27):
        drawdatapoint(d)
    for d in range(28, 44):
        drawdatapoint(d)

def count_paths(line, counters):
    index = line[0] + line[1]
    d = counters[index]
    key = line[6] + line[7]
    if (key) in d:
        d[key] = d.get(key, 0) + 1
    else: 
        d[key] = 1

def analyze_drawings():
    counters = {}
    for i in range(1, 9):
        counters[str(i) + "v"] = dict()
        counters[str(i) + "t"] = dict()
        counters[str(i) + "b"] = dict()
        counters[str(i) + "p"] = dict()

    # for d in range(1, 27):
    data = alldrawingdsdata()
    for line in range(1, len(data)):
        print data[line]
        count_paths(data[line][0], counters)

    print counters

# if os.path.exists("output"):
#     raise Exception('delete output folder')
# os.makedirs("output")

# print datapoint(1)
# parse_directions()
# parse_slide_type_visited()
# parse_next_directions()
# parse_average_timing_per_slide_type()

# all_drawings()
analyze_drawings()


