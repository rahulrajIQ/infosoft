class DataStream:
    def __init__(self):
        self.data = dict()

    def should_output_data_str(self, timestamp: int, data_string: str) -> bool:

        if data_string in self.data and timestamp - self.data[data_string] < 5:
                return False

        else:
                self.data[data_string] = timestamp
                return True



if __name__ == "__main__":
        data_stream = DataStream()

        print(data_stream.should_output_data_str(timestamp=0,
        data_string="hello"))

        print(data_stream.should_output_data_str(timestamp=1,
        data_string="world"))

        print(data_stream.should_output_data_str(timestamp=6,
        data_string="hello"))

        print(data_stream.should_output_data_str(timestamp=7,
        data_string="hello"))

        print(data_stream.should_output_data_str(timestamp=8,
        data_string="world"))