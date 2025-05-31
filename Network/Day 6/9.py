from scapy.all import  HTTPRequest, rdpcap, IP, HTTPResponse
import datetime
import sys

try:
    if len(sys.argv) != 2:
        print("Usage: python 9.py <file>")
        sys.exit(1)
        pkt = rdpcap(sys.argv[1])
except Exception as e:
        print(f"Error {e}")

for p in pkt:
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if p.haslayer(HTTPRequest):
        try:
            s = p[IP]
            req = p[HTTPRequest]
            print(f'\n{s.src}:{s.sport} requested {req.Method.decode()} {req.Host.decode()}{req.Path.decode()} at {t} ({s.dst}:{s.dport})')
            if req.User_Agent:
                print(f'User_Agent: {req.User_Agent.decode()}')
            if req.Referer:
                print(f'Referer: {req.Referer.decode()}')
        except Exception as e:
             print(f"Error {e}")
    
    if p.haslayer(HTTPResponse):
        try:
            res =p[HTTPResponse]
            print(f'Response code: {res.Status_Code.decode()}')
            if res.Location:
                location = res.Location.decode("utf-8", errors="ignore")
                if "/" in location.split("://", 1)[-1].split("/", 1)[-1]:
                    print(f"Redirect URL at {t}: {location}")
            if res.Content_Disposition:
                print(f'Content_Disposition: {res.Content_Disposition.decode()}')        
            else:
                print("Content_Disposition: None")
            print(f'Content_Type: {res.Content_Type.decode()}') 
        except Exception as e:
            print(f"Error {e}")       
  
print("\nDone. End of pcap")