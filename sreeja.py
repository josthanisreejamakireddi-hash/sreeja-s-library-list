print("enter roll number start from 12")

libary_members= {13801: "ranjana",

                 13802:"juhith",

                 13803: "lahari",

                 13804: "mallika",

                 13805: "priya",

                 13806: "prabha sree"}

print("libary system")

try:

    roll_num=int(input("roll_num :"))

    name=input("name:")

    if roll_num in libary_members:

        print("member allready existe")

        print (f"roll number: (roll num)")

        print (f"name: [libary_members [roll_num]")

    else:

       print("new member found:updating")

       libary_members [roll_num]=name

       print("updated successfully")

       print("\n updated member")

       print (libary_members)

except valueerror:

    print("enter valid roll num")
