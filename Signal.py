import csv
import os
import glob

class Digital():
    def __init__(self, id, name, type, node_ip, address, status=False, comment=''):
        self.name = name       
        self.type = type            #Hardware signal type must be clear
        self.status =status         #Every switch/DigitalIO has a Value It is true or false
        self.address = address      #IO cards has an address. it is just to save it for better and easier maintenance
        self.force = False
        self.comment = comment      #Every sensor has a name in an industrial plan
        self.id = id
        self.node_ip = node_ip

    def Signal_status(self):
            return {"Force":self.force , "Status":self.status}

    def Signal_information(self):
        return {"ID":self.id, "Name":self.name, "Type":self.type, "Node Address":self.node_ip, "Address":self.address, "Status":self.status , "Force":self.force , "Comment":self.comment}
    
    def Signal_update(self,signal_value):
        if not self.force== False:
            self.status = signal_value
        else: pass

    def Signal_force(self, address_value, status, force=False):
        if not force:
            self.Signal_update(address_value)
        elif force:
            self.status = status
        self.force = force

    '''def Signal_logic(self):
        state= self.status
        if self.type == "NO" :
            return state("Status")
        elif self.type == "NC" :
            return not state("Status")'''

class Analog():
    def __init__(self, id, name, type, node_ip, address, bit_rate, physical_range='', unit = '', value= 0, comment= '' ): #, status
        self.id = id                    #An ID has to be assigned to every input or output signal
        self.name = name                #Every sensor has a name in an industrial plan
        self.type = type                #Hardware signal type must be clear
        self.address = address          #IO cards has an address. it is just to save it for better and easier maintenance
        self.bit_rate = bit_rate        #the Analog signal resolution
        #self.status =status
        self.value = value              #Every AnalogIO has a value
        self.force = False
        self.node_ip = node_ip
        self.physical_range = physical_range
        self.unit = unit
        self.comment = comment

    def Signal_status(self):
            return {"Force":self.force , "Value":self.value} #"Status":self.status ,

    def Signal_information(self):
        return {"ID":self.id, "Name":self.name, "Type":self.type, "Node_Address":self.node_ip, "Address":self.address, "Bit Rate":self.bit_rate, "Physical Range":self.physical_range, "Unit":self.unit, "Force":self.force ,"Value":self.value, "Comment":self.comment} #"Status":self.status ,
    
    def Signal_update(self,signal_value):
        if not self.force:
            self.value = signal_value
        else: pass

    def Signal_force(self,address_value, signal_value, force=False):
        if not force:
            self.force = force
            self.Signal_update(address_value)
            #print("Update")
        elif force == True:
            self.value = signal_value
        self.force = force

    def Scale(self, Y0, Y1, X0, X1):
        m = ( Y1 - Y0 )/ (X1 - X0)
        return m*(self.value - X0 )+ Y0

'''class STG():                    #Signal Table Generator
    def __init__(self, file_address):
        self.file_address = file_address
        self.table = dict()
        try:
            file_name = self.file_address
            while file_name.find("/"):
                file_name = [file_name.find("/")+1:]

            temp = os.getcwd()
            os.chdir(self.file_address - file_name)
            with open(file_name, newline='') as Sigs:
                Sig_info = csv.reader(Sigs, delimiter=' ', quotechar=',')
                for row in Sig_info:
                    self.table.get(row.)
        except:
            print("An error accured.\nFile name:%s\nPlease Check the file and also the address." %(self.address))
        finally:
            pass'''
        
class Process_Image():
    def __init__(self):
        pass

    def Read_DI(self):
        pass

    def Read_AI(self):
        pass

    def Write_DO(self):
        pass
    
    def Write_AO(self):
        pass
