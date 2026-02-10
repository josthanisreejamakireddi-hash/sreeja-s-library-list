print("caution please enter roll number start from 12")

libary_members= {12800: "balu",

                 12801:"lokesh",

                 12802: "ramesh",

                 12803: "sai",

                 12804: "pavan",

                 12805: "raj kumar"}

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
