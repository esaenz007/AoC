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
        number = None
        signals = [x for x in signals]
        segments = [v for k,v in self.signal_wiring.items() if k in signals]
        segments.sort()
        found_number = [i for i,v in enumerate(self.digits_segments_map) if v == segments]
        if len(found_number) == 1:
            number = found_number[0]
        return number

    def get_segments(self,number):
        return self.digits_segments_map[number]

    def get_segment_signal(self,segment):
        signal = [k for k,v in self.signal_wiring.items() if v == segment]
        return signal[0] if len(signal) == 1 else None    

    def get_signals(self,number):
        return "".join( [k for k,v in self.signal_wiring.items() if v in self.get_segments(number)])

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