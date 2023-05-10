#Zarif M Quamrul 
#010319619
import csv
import Package
import datetime
import Truck
import ChainingHashTable
from builtins import ValueError

#Reading the CSV files for the data provided
with open("Address_File.csv") as csvfile1:
    address_data = list(csv.reader(csvfile1))

with open("Package_File.csv") as csvfile2:
    package_data = list(csv.reader(csvfile2))

with open("Distance_File.csv") as csvfile3:
    distance_data = list(csv.reader(csvfile3))

#Time Complexity O(1)
#Space Complexity O(n)
#Loop through the CSV data and use data to create package objects and insert into hash table
def add_packages_HT(CSV_data, package_HT):
    for package in CSV_data:
        package_ID = int(package[0])
        package_object =  Package.Package(package[0], package[1],package[2],package[3],package[4],package[5],package[6])

        #insert into hashtable
        package_HT.insert(package_ID,package_object)

#Create package hash table
package_hash_table = ChainingHashTable.ChainingHashTable()

#insert package data from csv to hash table
add_packages_HT(package_data,package_hash_table)

# Create truck object truck1
delivery_truck1 = Truck.Truck(16, 18, None, [1, 13, 14, 15, 16,19, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8,minutes=0))

# Create truck object truck2
delivery_truck2 = Truck.Truck(16, 18, None, [3, 6, 9, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,"4001 South 700 East",
                              datetime.timedelta(hours=10,minutes=20))

# Create truck object truck3
delivery_truck3 = Truck.Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9,minutes=5))
#Time complexity --> O(1)
#Space Complexity --> O(n)
#Method to calculate distance between two addresses
def distance_between(curr,target):
    retrieved_distance = distance_data[curr][target]
    if retrieved_distance == "":
        retrieved_distance = distance_data[target][curr]
    return float(retrieved_distance)
#Time complexity --> O(n)
#Space Complexity --> O(n)
#Method searches through the CSV to find the address and returns the ID of the address if found
def find_address_ID(address):
    for each in address_data:
        if address in each[2]:
            return int(each[0])

#Time complexity --> O(n^2)
#Space Complexity --> O(n)
def organize_and_ship(truck_object):
    to_be_delivered = []

    #Retrieve each package object by the package ids from the truck object
    #add them to the list of packages to be delivered
    for package_ID in truck_object.packages:
        to_be_delivered.append(package_hash_table.search(package_ID))
    #clear the package list in truck for the new organized package list
    truck_object.packages = []

    while len(to_be_delivered) > 0:
        #Initialize next address to an excess amount to help find the closest address
        #Initialize empty variable to hold the appropriate next package to be added to organized list
        next_address = 2000
        next_package = None

        for package in to_be_delivered:
            if distance_between(find_address_ID(truck_object.address),find_address_ID(package.delivery_address)) <= next_address :
                next_address = distance_between(find_address_ID(truck_object.address),find_address_ID(package.delivery_address))
                next_package = package
        #Add the closest package to the trucks package list
        truck_object.packages.append(next_package.ID)
        #Remove the package from the to be delivered list
        to_be_delivered.remove(next_package)
        #Add the distance to the next address to the truck mileage
        truck_object.mileage += next_address
        #Update the truck's address to the address of the package after delivery
        truck_object.address = next_package.delivery_address
        #Adjust time for truck by calculating time = distance / speed
        truck_object.time += datetime.timedelta(hours= next_address/18)
        #Update package time to track status of package delivery
        next_package.delivery_time = truck_object.time
        next_package.departure_time = truck_object.depart_time

organize_and_ship(delivery_truck1)

organize_and_ship(delivery_truck2)

delivery_truck3.depart_time = min(delivery_truck1.time, delivery_truck2.time)
delivery_truck3.time = delivery_truck3.depart_time
organize_and_ship(delivery_truck3)

class Main:
    print("========================================================")
    print("Name: Zarif M Quamrul")
    print("StudentID: 010319619")
    print("C950: Data Structures and Algorithms II [NHP2]")
    print("Western Governors University Parcel Service (WGUPS)")
    print(f"Total mileage of delivery trucks: {delivery_truck1.mileage + delivery_truck2.mileage + delivery_truck3.mileage}")
    print("========================================================")

    text = input("To start please type the word 'Start' (All else will cause the program to quit).")
    # If the user doesn't type "leave" the program will ask for a specific time in regard to checking packages
    if text == "Start":
        try:
            # The user will be asked to enter a specific time
            user_time = input("Please enter a time to check status of package(s). Use the following format, HH:MM:SS")
            (hours, mins, secs) = user_time.split(":")
            convert_timedelta = datetime.timedelta(hours=int(hours), minutes=int(mins), seconds=int(secs))
            # The user will be asked if they want to see the status of all packages or only one
            second_input = input("To view the status of an individual package please type 'single'. For a rundown of all"
                                 " packages please type 'all'.")
            # If the user enters "single" the program will ask for one package ID
            if second_input == "single":
                try:
                    # The user will be asked to input a package ID. Invalid entry will cause the program to quit
                    single_input = input("Enter the numeric package ID")
                    package = package_hash_table.search(int(single_input))
                    package.update_status(convert_timedelta)
                    print(str(package))
                except ValueError:
                    print("Entry invalid. Closing program.")
                    exit()
            # If the user types "all" the program will display all package information at once
            elif second_input == "all":
                try:
                    for packageID in range(1, 41):
                        package = package_hash_table.search(packageID)
                        package.update_status(convert_timedelta)
                        print(str(package))
                except ValueError:
                    print("Entry invalid. Closing program.")
                    exit()
            else:
                exit()
        except ValueError:
            print("Entry invalid. Closing program.")
            exit()
    elif input != "time":
        print("Entry invalid. Closing program.")
        exit()
