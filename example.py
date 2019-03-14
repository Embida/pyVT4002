import VT4002
import time

if __name__ == '__main__':
    print("Example started....")
    vt4002 = VT4002.Connection(port='/dev/ttyS10')
    output = vt4002.get_actual_values()
    print(output.temp2_actual())
    print(output.temp1_actual())
    vt4002.set_nominal_values(30)

    vt4002.start_program(1)
    time.sleep(5)
    vt4002.stop_program()
