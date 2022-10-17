import random

boxes = []
papers = []
number_of_prisoner = 100


def open_box(box_number, prisoner_number, count_ciclo):
    if prisoner_number == boxes[box_number]:
        print("Prisoner: " + str(prisoner_number) + " found his number in the box: " + str(box_number)
              + " in the cycle: " + str(count_ciclo))
    else:
        # print("NOT Found, the box: " + str(box_number) + " has the paper: " + str(boxes[box_number])
        # + ", the cycle is: " + str(count_ciclo))
        count_ciclo += 1
        open_box(boxes[box_number], prisoner_number, count_ciclo)


# Setup: papers array
for x in range(number_of_prisoner):
    papers.append(x)

# Setup: Randomly put one paper in each box
for x in range(number_of_prisoner):
    paper_in_box = random.randrange(0, len(papers))
    # print("position:\t" + str(paper_in_box) + "\t number:\t" + str(papers[paper_in_box]))
    boxes.append(papers[paper_in_box])
    papers.pop(paper_in_box)

# Setup: Show the pairs box - paper
for x in range(number_of_prisoner):
    print("in the box:\t" + str(x) + "\tthe paper number is:\t" + str(boxes[x]))

# Prisoners opening boxes
for x in range(number_of_prisoner):
    open_box(x, x, 1)
