class Digital():

    def __init__(self, id, name, type, address, status=False):
        self.id = id                #An ID has to be assigned to every input or output signal
        self.name = name            #Every sensor has a name in an industrial plan
        self.type = type            #Every switch/DigitalIO is Normal Open or Normal closed
        self.status =status         #Every switch/DigitalIO has a Value It is true or false
        self.address = address      #IO cards has an address. it is just to save it for better and easier maintenance
        self.force = False
        
    def Signal_status(self):
            return {"Force":self.force , "Status":self.status}

    def Signal_information(self):
        return {"ID":self.id, "Name":self.name, "Type":self.type, "Address":self.address,"Status":self.status ,"Force":self.force }
    
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

    def Signal_logic(self):
        state= self.status
        if self.type == "NO" :
            return state("Status")
        elif self.type == "NC" :
            return not state("Status")

class Analog():
    def __init__(self, id, name, type, address, bit_rate, value= 0): #, status
        self.id = id                    #An ID has to be assigned to every input or output signal
        self.name = name                #Every sensor has a name in an industrial plan
        self.type = type                #Every AnalogIO has an electrical type(4 to 20 mA or 0 to 5 Volts or 0 to 10 Volts ...)
        self.address = address          #IO cards has an address. it is just to save it for better and easier maintenance
        self.bit_rate = bit_rate        #the Analog signal resolution
        #self.status =status
        self.value = value              #Every AnalogIO has a value
        self.force = False

    def Signal_status(self):
            return {"Force":self.force , "Value":self.value} #"Status":self.status ,

    def Signal_information(self):
        return {"ID":self.id, "Name":self.name, "Type":self.type, "Address":self.address, "Bit Rate":self.bit_rate,
                "Force":self.force ,"Value":self.value} #"Status":self.status ,
    
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
