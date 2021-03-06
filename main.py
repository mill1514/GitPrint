import letters as l
import datetime as dt
import subprocess as sp
import os

message = "hello"

# preprocessing for determining pixel
today = dt.date.today()
startdate = dt.date(2018, 4, 15)    # Set this to the sunday you'd like to start on
                                    # (Github week starts Sunday)
daysrunning = (today - startdate).days

# Do the junk
def main():
    
    currletterindex = (int) (daysrunning / 49)
    currweekindex = (int) ( (daysrunning % 49) / 7 )
    currpixelindex = daysrunning % 7

    #print("Days since start:", daysrunning);
    #print("Current letter:", message[currletterindex]);

    # Calculate whether or not to 'commit' today
    alpha = ord(message[currletterindex]) - 96
    currletter = l.getLetter(alpha)
    currpixel = currletter[currpixelindex][currweekindex]

    #print("currletter:", alpha, currletter);
    #print("currweek:", currweekindex, currletter[currpixelindex]);
    #print("currpixel:", currpixelindex, currpixel);

    if currpixel:
        print("COMMIT")
        os.chdir("./GitPrint")
        sp.call("./phoneycommit.sh")
        sp.call("./phoneycommit.sh")
        sp.call("./phoneycommit.sh")
        
    else:
        print("DON'T COMMIT")

    return

main()
