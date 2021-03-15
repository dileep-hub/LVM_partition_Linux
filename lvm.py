import os

print("\t\t\t\t WELCOME ")
print("\t\t\t--------------------------")

print("""\t\t\t
\t\t\tPress 1 : to create a Logical Volume
\t\t\tPress 2 : to extend the Logical Volume
\t\t\tpress 3 : TO EXIT

""")

def lvm_partition():

        no_of_pv = input("\t\tEnter the no of pv to be created: ")
        no_of_pv = int(no_of_pv)
        print("\n\nFrom this select the disks u need to create the pv: ")
        print("\t\t\t--------------------------------------")
        os.system("\n\nfdisk -l")
        PV = []
        for i in range(no_of_pv):
                disk_name = input("\n\n\nEnter the name of disk{}: ". format(i+1))
                PV.append(disk_name)
                print("\ncreating physical volume.....")

                os.system("pvcreate {}". format(PV[i]))
                print("\t\t\t--------------------------------------")
                print("\nDisplaying Physical Volume.....")
                os.system("pvdisplay {}". format(PV[i]))
                print("\t\t\t--------------------------------------")

        vg_name = input("\n\nEnter the name for the volume group: ")
        vg_disk = ""
        for i in PV:
                vg_disk = vg_disk + " " + i
                print("\t\t\t--------------------------------------")

        print("\n\nCreating new Volume Group...")
        os.system("vgcreate {} {} ". format(vg_name, vg_disk))
        print("\t\t\t--------------------------------------")
        print("\n\nDisplaying vg...../ ")
        os.system("vgdisplay {}". format(vg_name))
        print("\t\t\t--------------------------------------")

        lv_name = input("\n\nEnter a name for Logical volume: ")
        lv_size = input("\n\nEnter the partition size to be created in Gib: ")
        lv_size = int(lv_size)
        print("\t\t\t--------------------------------------")
        print("\n creating Logical volume...")
        os.system("lvcreate --size {}G --name {} {}". format(lv_size, lv_name, vg_name))
        print("\t\t\t--------------------------------------")
        print("\n\nDisplaying Logical Volume...")
        os.system("lvdisplay {}/{}". format(vg_name, lv_name))
        print("\t\t\t--------------------------------------")
        print("\n\nformatting....")
        os.system("mkfs.ext4 /dev/{}/{}". format(vg_name, lv_name))
        print("\t\t\t--------------------------------------")
        print("\n\nMounting the partition to the folder...")
        fold_name = input("Enter the folder name to be created: ")
        os.system("mkdir /{}". format(fold_name))
        print("\t\t\t--------------------------------------")
        print("\n\nmounting......")
        os.system("mount /dev/{}/{}  /{}". format(vg_name, lv_name, fold_name))
        print("\t\t\t--------------------------------------")
        print("\n\nstatus of mounting....")
        os.system("df -h")

        print("\t\t\t*********************************")
        print("\t\t\tSuccessfull created Logical Volume")


def ext_partition():
        print("ext")
        lv_ext_name = input("\n\nEnter the name of Logical Volume to be extended with the root folder.....: ")
        lv_ext_size = input("\nHow much size should u extend [Gib]: ")
        #lv_ext_size = int(lv_ext_size)
        print("\t\t\t--------------------------------------")
        print("\n\nExtending volume..../-")
        os.system("lvextend --size +{} {}". format(lv_ext_size, lv_ext_name))
        print("\t\t\t--------------------------------------")
        print("\n\nNow in the below status u can see still size not increased..")
        os.system("df -h")
        print("\t\t\t--------------------------------------")
        print("\n\nformating the extending space../-")
        os.system("resize2fs {}". format(lv_ext_name))
        print("NOw u can see it is extended..")
        os.system("df -h")

        print("\t\t\t**********************************")
        print("Successfully Extended the Logical Volume")



opt = input("Enter ur choice:")
opt = int(opt)


if (opt == 1):
        lvm_partition()

elif (opt == 2):
        ext_partition()

elif (opt == 3):
        exit()

else:
        print("Invalid input")
