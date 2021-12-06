class LineChart(object):
    def __init__(self,width:int,height:int):
        self.points = []
        for h in range(height):
            self.points.append([0 for x in range(width)])

    def draw_line(self,x1,y1,x2,y2):
        slope = 0
        line_type = ""

        if y1 == y2:
            line_type = "horizontal"
        elif x1 == x2:
            line_type = "vertical"
        else:
            line_type = "diagonal"
            slope = 1 if y1<y2 else -1
        
        self.points[y1][x1] += 1

        while True:
            if line_type in ["horizontal","diagonal"]:
                if x2>x1:
                    x1 += 1
                else:
                    x1 -= 1
                y1 += slope
            elif line_type == "vertical":
                if y2>y1:
                    y1 += 1
                else:
                    y1 -= 1

            self.points[y1][x1] += 1

            if x1==x2 and y1==y2:
                break

    def get_dangerous_point_count(self):
        return sum( [ len( [y for y in x if y > 1])for x in self.points])

    def print_chart(self):
        for x in self.points:
            print("".join([str(y) if y > 0 else "." for y in x] ))