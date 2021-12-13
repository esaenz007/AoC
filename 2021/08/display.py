class SevenSegmentDisplay(object):
    
    def __init__(self):
        
        self.digits_segments_map = [
            [1,2,3,5,6,7],  # 0
            [3,6],          # 1
            [1,3,4,5,7],    # 2
            [1,3,4,6,7],    # 3
            [2,3,4,6],      # 4
            [1,2,4,6,7],    # 5,
            [1,2,4,5,6,7] , # 6,
            [1,3,6],        # 7,
            [1,2,3,4,5,6,7],# 8,
            [1,2,3,4,6,7]   # 9
        ]
        self.signal_wiring = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}

    def get_number(self,signals):
        digits = list(reversed( signals.split(" ")))
        number = None
        for i,d in enumerate( digits):
            signals = [x for x in d]
            segments = [v for k,v in self.signal_wiring.items() if k in d]
            segments.sort()
            number_map = [i for i,v in enumerate(self.digits_segments_map) if v == segments]
            if len(number_map) == 1:
                number = 0 if number is None else number
                number += number_map[0] if i == 0 else number_map[0] * pow(10,i)
        return number

    def get_segments(self,number):
        return self.digits_segments_map[number]

    def get_segment_signal(self,segment):
        for k,v in self.signal_wiring.items():
            if v == segment:
                return k

    def get_signals(self,number):
        segments = self.get_segments(number)
        signals = "".join( [k for k,v in self.signal_wiring.items() if v in segments])
        return signals

    def swap_signals(self,signal1,signal2):
        tmp = self.signal_wiring[signal1]
        self.signal_wiring[signal1] = self.signal_wiring[signal2]
        self.signal_wiring[signal2] = tmp

    def rewire_number(self,number,signals):
        current_wiring = self.get_signals(number)
        source_wires = list(set(signals)-set(current_wiring))
        target_wires = list(set(current_wiring)-set(signals))
        for i,x in enumerate(source_wires):
            self.swap_signals(x, target_wires[i])
