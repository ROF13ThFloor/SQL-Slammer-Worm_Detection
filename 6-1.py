import pyshark
import csv  
import collections
import os 

def sh(script):
    os.system("bash -c '%s'" % script)


caps = pyshark.FileCapture('200302161400.dump' ,  display_filter='(udp) and (not udp.port==53 and not udp.port==67 and not udp.port==68 and not icmp)')
cntr = 0 
src_ips = []
dst_ips = []
src_ports = []
dst_ports = []

# with open('data.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['srcip' , 'dstip' , 'srcport' , 'dstport' , 'srcmac' , 'dstmac'])
#     for c in caps:  
        
#         row = []
#         row.append(c['ip'].src)
#         row.append(c['ip'].dst)
#         row.append(c['udp'].srcport)
#         row.append(c['udp'].dstport)
#         # row.append(c['eth'].src)
#         # row.append(c['eth'].dst)
#         writer.writerow(row)
#         cntr = cntr + 1 

# with open('mac.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['srcMAC' , 'dstMAC'])
#     for c in caps:  
#         row = []
#         row.append(c['eth'].src)
#         row.append(c['eth'].dst)
#         writer.writerow(row)
#         cntr = cntr + 1 

# with open('Part4.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['srcIP' , 'dstIP'])
#     for c in caps:  
#         row = []
#         row.append(c['ip'].src)
#         row.append(c['ip'].dst)
#         writer.writerow(row)
         


print("number of suspicious packages is ==> ")

sh("wc -l data.csv")
with open('data.csv') as f:
    next(f) # Skip the first line
    print("most 10 dst port use in network ==> " , collections.Counter(line.rstrip().rpartition(',')[-1] for line in f).most_common(10) )



with open('Part4.csv') as f:
    next(f) # Skip the first line
    print("most 10 ip in network ==> " , collections.Counter(line.rstrip().rpartition(',')[0] for line in f).most_common(10)  )



with open('mac.csv') as f:
    next(f) # Skip the first line
    print("most 10 mac src use in network ==> " , collections.Counter(line.rstrip().rpartition(',')[0] for line in f).most_common(10) )


with open('Part4.csv') as f:
    next(f) # Skip the first line
    print("most 7 pair ip in network ==> " , collections.Counter(line for line in f).most_common(7) )
