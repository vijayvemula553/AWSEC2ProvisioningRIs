import boto3
import json
from os import listdir
from os import rename
from pathlib import Path
import random


loadSamples = False


class IOffering():
    AvailabilityZone = None
    Duration = None
    FixedPrice = None
    InstanceType = None
    ProductDescription = None
    ReservedInstancesOfferingId = None
    UsagePrice = None
    CurrencyCode = None
    InstanceTenancy = None
    Marketplace = None
    OfferingClass = None
    OfferingType = None
    PricingDetails = None
    RecurringFrequency = None
    RecurringAmount = None
    Scope = None

    EffectiveHourlyRate = None

    def __init__(self):
        self.AvailabilityZone = None
        self.Duration = None
        self.FixedPrice = None
        self.InstanceType = None
        self.ProductDescription = None
        self.ReservedInstancesOfferingId = None
        self.UsagePrice = None
        self.CurrencyCode = None
        self.InstanceTenancy = None
        self.Marketplace = None
        self.OfferingClass = None
        self.OfferingType = None
        self.PricingDetails = None
        self.RecurringFrequency = None
        self.RecurringAmount = None
        self.Scope = None

        self.EffectiveHourlyRate = None

    def getJson(self):
        data = {
            "AvailabilityZone": self.AvailabilityZone,
            "Duration": self.Duration,
            "FixedPrice": self.FixedPrice,
            "InstanceType": self.InstanceType,
            "ProductDescription": self.ProductDescription,
            "ReservedInstancesOfferingId": self.ReservedInstancesOfferingId,
            "UsagePrice": self.UsagePrice,
            "CurrencyCode": self.CurrencyCode,
            "InstanceTenancy": self.InstanceTenancy,
            "Marketplace": self.Marketplace,
            "OfferingClass": self.OfferingClass,
            "OfferingType": self.OfferingType,
            "PricingDetails": self.PricingDetails,
            "RecurringFrequency": self.RecurringFrequency,
            "RecurringAmount": self.RecurringAmount,
            "Scope": self.Scope,
            "EffectiveHourlyRate": self.EffectiveHourlyRate
        }
        return data

    def print(self):
        print("{")
        print("\tAvailabilityZone:", self.AvailabilityZone)
        print("\tDuration:", self.Duration)
        print("\tFixedPrice:", self.FixedPrice)
        print("\tInstanceType:", self.InstanceType)
        print("\tProductDescription:", self.ProductDescription)
        print("\tReservedInstancesOfferingId:",
              self.ReservedInstancesOfferingId)
        print("\tUsagePrice:", self.UsagePrice)
        print("\tCurrencyCode:", self.CurrencyCode)
        print("\tInstanceTenancy:", self.InstanceTenancy)
        print("\tMarketplace:", self.Marketplace)
        print("\tOfferingClass:", self.OfferingClass)
        print("\tOfferingType:", self.OfferingType)
        print("\tPricingDetails:", self.PricingDetails)
        print("\tRecurringFrequency:", self.RecurringFrequency)
        print("\tRecurringAmount:", self.RecurringAmount)
        print("\tScope:", self.Scope)
        print("\tEffectiveHourlyRate:",  self.EffectiveHourlyRate)
        print("},")

    def getKwargs(self, dryRun):
        print("DryRun:", dryRun)
        d = {}
        d["InstanceCount"] = 1
        d["ReservedInstancesOfferingId"] = self.ReservedInstancesOfferingId
        d["DryRun"] = dryRun
        return d


class AvailabilityZone():
    Number = None
    ordered = None
    Name = None

    def __init__(self):
        self.Name = None
        self.Number = None
        self.ordered = None

    def print(self):
        print("{")
        print("\tName:", self.Name)
        print("\tNumber:", self.Number)
        print("\tordered:", self.ordered)
        print("}")

    def getJson(self):
        return {
            "Name": self.Name,
            "Number": self.Number,
            "ordered": self.ordered
        }


class Order():
    aws_access_key_id = None
    aws_secret_access_key = None
    Number = None
    ordered = None
    fileName = None
    Region = None
    IncludeMarketplace = None
    InstanceType = None
    MaxDuration = None
    MaxInstanceCount = None
    MinDuration = None
    ProductDescription = None
    InstanceTenancy = None
    OfferingType = None
    OfferingClass = None
    isFixedPrice = None
    isHourlyPrice = None
    MaxFixedPrice = None
    MaxHourlyPrice = None
    DryRun = None

    AvailabilityZones = []
    PurchasedInstances = []

    def __init__(self):

        self.aws_access_key_id = None
        self.aws_secret_access_key = None
        self.Number = None
        self.ordered = None
        self.fileName = None
        self.Region = None
        self.IncludeMarketplace = None
        self.InstanceType = None
        self.MaxDuration = None
        self.MaxInstanceCount = None
        self.MinDuration = None
        self.ProductDescription = None
        self.InstanceTenancy = None
        self.OfferingType = None
        self.OfferingClass = None

        self.isFixedPrice = None
        self.isHourlyPrice = None
        self.MaxFixedPrice = None
        self.MaxHourlyPrice = None

        self.DryRun = None
        self.PurchasedInstances = []

        self.AvailabilityZones = []

    def getPurchasedInstancesJson(self):
        arrayJson = []
        for pi in self.PurchasedInstances:
            arrayJson.append(pi.getJson())
        return arrayJson

    def getAvailabilityZonesJson(self):
        arrayJson = []
        for az in self.AvailabilityZones:
            arrayJson.append(az.getJson())
        return arrayJson

    def getJson(self):
        return {

            "aws_access_key_id": self.aws_access_key_id,
            "aws_secret_access_key": self.aws_secret_access_key,
            "Number": self.Number,
            "ordered": self.ordered,
            "Region": self.Region,
            "IncludeMarketplace": self.IncludeMarketplace,
            "InstanceType": self.InstanceType,
            "MaxDuration": self.MaxDuration,
            "MaxInstanceCount": self.MaxInstanceCount,
            "MinDuration": self.MinDuration,
            "ProductDescription": self.ProductDescription,
            "InstanceTenancy": self.InstanceTenancy,
            "OfferingType": self.OfferingType,
            "OfferingClass": self.OfferingClass,
            "DryRun": self.DryRun,
            "isFixedPrice": self.isFixedPrice,
            "isHourlyPrice": self.isHourlyPrice,
            "MaxFixedPrice": self.MaxFixedPrice,
            "MaxHourlyPrice": self.MaxHourlyPrice,
            "AvailabilityZones": self.getAvailabilityZonesJson(),
            "PurchasedInstances": self.getPurchasedInstancesJson()
        }

    def getKwargs(self, az):
        d = {}
        if self.InstanceType is not None:
            d["InstanceType"] = self.InstanceType
        if self.IncludeMarketplace is not None:
            d["IncludeMarketplace"] = self.IncludeMarketplace
        else:
            d["IncludeMarketplace"] = True
        if self.MaxDuration is not None:
            d["MaxDuration"] = self.MaxDuration
        if self.MaxInstanceCount is not None:
            d["MaxInstanceCount"] = self.MaxInstanceCount
        if self.MinDuration is not None:
            d["MinDuration"] = self.MinDuration
        if self.ProductDescription is not None:
            d["ProductDescription"] = self.ProductDescription
        if self.OfferingClass is not None:
            d["OfferingClass"] = self.OfferingClass
        if self.InstanceTenancy is not None:
            d["InstanceTenancy"] = self.InstanceTenancy
        if self.OfferingType is not None:
            d["OfferingType"] = self.OfferingType

        # something something filter something something complete
        if az is not None:
            d["Filters"] = [
                {
                    'Name': 'availability-zone',
                    'Values': [
                        az
                    ]
                }
            ]
        return d

    def print(self):
        print("Number:", self.Number)
        print("ordered:", self.ordered)
        print("fileName:", self.fileName)
        print("Region:", self.Region)
        # print("AvailabilityZone:", self.AvailabilityZone)
        print("IncludeMarketplace:", self.IncludeMarketplace)
        print("InstanceType:", self.InstanceType)
        print("MaxDuration:", self.MaxDuration)
        print("MaxInstanceCount:", self.MaxInstanceCount)
        print("MinDuration:", self.MinDuration)
        print("ProductDescription:", self.ProductDescription)
        print("InstanceTenancy:", self.InstanceTenancy)
        print("OfferingType:", self.OfferingType)
        print("DryRun:", self.DryRun)
        print("OfferingClass:", self.OfferingClass)
        print("AvailabilityZones: [")
        for az in self.AvailabilityZones:
            az.print()
        print("]")
        print("PurchasedInstances: [")
        for pi in self.PurchasedInstances:
            pi.print()
        print("]")


def getInstanceOffering(instanceOffering):
    currentIOffering = IOffering()
    currentIOffering.Scope = instanceOffering['Scope']

    if currentIOffering.Scope == "Availability Zone":
        # will throw if scope is region and not availability zone
        currentIOffering.AvailabilityZone = instanceOffering['AvailabilityZone']
    currentIOffering.Duration = instanceOffering['Duration']
    currentIOffering.FixedPrice = instanceOffering['FixedPrice']
    currentIOffering.InstanceType = instanceOffering['InstanceType']
    currentIOffering.ProductDescription = instanceOffering['ProductDescription']
    currentIOffering.ReservedInstancesOfferingId = instanceOffering[
        'ReservedInstancesOfferingId']
    currentIOffering.UsagePrice = instanceOffering['UsagePrice']
    currentIOffering.CurrencyCode = instanceOffering['CurrencyCode']
    currentIOffering.InstanceTenancy = instanceOffering['InstanceTenancy']
    currentIOffering.Marketplace = instanceOffering['Marketplace']
    currentIOffering.OfferingClass = instanceOffering['OfferingClass']
    currentIOffering.OfferingType = instanceOffering['OfferingType']
    currentIOffering.PricingDetails = instanceOffering['PricingDetails']

    # Try to get the effective hourly rate
    durationInHours = currentIOffering.Duration/360
    effectivePerHour = 0
    # Do we have a recurring charge of hourly for this instance type
    try:
        RecurringCharges = instanceOffering["RecurringCharges"]
        currentIOffering.RecurringFrequency = RecurringCharges[0]['Frequency']
        currentIOffering.RecurringAmount = RecurringCharges[0]['Amount']
        effectivePerHour += currentIOffering.RecurringAmount
        # print("Recurring per hour:", currentIOffering.RecurringAmount)
    except:
        pass

    # Do we have a fixed price for this instance type

    if currentIOffering.FixedPrice != 0.0:
        effectivePerHour += currentIOffering.FixedPrice/durationInHours
        # print("FixedPrice per hour:", currentIOffering.FixedPrice/durationInHours)

    currentIOffering.EffectiveHourlyRate = effectivePerHour
    # print("Total Effective Rate:", currentIOffering.EffectiveHourlyRate, "\n")

    # currentIOffering.print()
    return currentIOffering


def parseInstanceOffering(dic):
    iOffering = IOffering()
    try:
        iOffering.AvailabilityZone = dic["AvailabilityZone"]
    except:
        pass
    try:
        iOffering.Duration = dic["Duration"]
    except:
        pass
    try:
        iOffering.FixedPrice = dic["FixedPrice"]
    except:
        pass
    try:
        iOffering.InstanceType = dic["InstanceType"]
    except:
        pass
    try:
        iOffering.ProductDescription = dic["ProductDescription"]
    except:
        pass
    try:
        iOffering.ReservedInstancesOfferingId = dic["ReservedInstancesOfferingId"]
    except:
        pass
    try:
        iOffering.UsagePrice = dic["UsagePrice"]
    except:
        pass
    try:
        iOffering.CurrencyCode = dic["CurrencyCode"]
    except:
        pass
    try:
        iOffering.InstanceTenancy = dic["InstanceTenancy"]
    except:
        pass
    try:
        iOffering.Marketplace = dic["Marketplace"]
    except:
        pass
    try:
        iOffering.OfferingClass = dic["OfferingClass"]
    except:
        pass
    try:
        iOffering.OfferingType = dic["OfferingType"]
    except:
        pass
    try:
        iOffering.PricingDetails = dic["PricingDetails"]
    except:
        pass
    try:
        iOffering.RecurringFrequency = dic["RecurringFrequency"]
    except:
        pass
    try:
        iOffering.RecurringAmount = dic["RecurringAmount"]
    except:
        pass
    try:
        iOffering.Scope = dic["Scope"]
    except:
        pass
    try:
        iOffering.EffectiveHourlyRate = dic["EffectiveHourlyRate"]
    except:
        pass
    return iOffering


def parseAvailabilityZone(dic):
    az = AvailabilityZone()
    try:
        az.Name = dic["Name"]
    except:
        pass
    try:
        az.Number = dic["Number"]
    except:
        pass
    try:
        az.ordered = dic["ordered"]
    except:
        pass

    return az


def getNewOrder(individualOrder):
    currentOrder = Order()

    try:
        currentOrder.aws_access_key_id = individualOrder['aws_access_key_id']
    except:
       pass
    try:
        currentOrder.aws_secret_access_key = individualOrder['aws_secret_access_key']
    except:
       pass
    try:
        currentOrder.InstanceType = individualOrder['InstanceType']
    except:
        pass
    try:
        currentOrder.Region = individualOrder['Region']
    except:
        pass
    try:
        currentOrder.Number = individualOrder['Number']
    except:
        pass
    try:
        currentOrder.IncludeMarketplace = individualOrder['IncludeMarketplace']
    except:
        pass
    try:
        currentOrder.InstanceType = individualOrder['InstanceType']
    except:
        pass
    try:
        currentOrder.MaxDuration = individualOrder['MaxDuration']
    except:
        pass
    try:
        currentOrder.MaxInstanceCount = individualOrder['MaxInstanceCount']
    except:
        pass
    try:
        currentOrder.MinDuration = individualOrder['MinDuration']
    except:
        pass
    try:
        currentOrder.ProductDescription = individualOrder['ProductDescription']
    except:
        pass
    try:
        currentOrder.InstanceTenancy = individualOrder['InstanceTenancy']
    except:
        pass
    try:
        currentOrder.OfferingType = individualOrder['OfferingType']
    except:
        pass
    try:
        currentOrder.OfferingClass = individualOrder['OfferingClass']
    except:
        pass
    try:
        currentOrder.ordered = individualOrder['ordered']
    except:
        pass
    try:
        currentOrder.DryRun = individualOrder['DryRun']
    except:
        pass
    try:
        # currentOrder.PurchasedInstances = individualOrder['PurchasedInstances']
        for purchasedInstance in individualOrder['PurchasedInstances']:
            # try to parse in a purchased order
            pi = parseInstanceOffering(purchasedInstance)
            currentOrder.PurchasedInstances.append(pi)
    except:
        pass

    try:
        # availabilityZones
        for availabilityZone in individualOrder['AvailabilityZones']:
            az = parseAvailabilityZone(availabilityZone)
            currentOrder.AvailabilityZones.append(az)
    except:
        pass

    try:
        currentOrder.isFixedPrice = individualOrder['isFixedPrice']
    except:
        pass
    try:
        currentOrder.isHourlyPrice = individualOrder['isHourlyPrice']
    except:
        pass
    try:
        currentOrder.MaxFixedPrice = individualOrder['MaxFixedPrice']
    except:
        pass
    try:
        currentOrder.MaxHourlyPrice = individualOrder['MaxHourlyPrice']
    except:
        pass

    currentOrder.print()

    return currentOrder


def attemptPurchases(order):
    """code for attempting purchases for an order"""
    print("\n")
    # here we sort out the availability zones
    hasOrdersAssigned = True

    for az in order.AvailabilityZones:
        if az.ordered is None:
            az.ordered = 0
        if az.Number is None:
            hasOrdersAssigned = False

    if hasOrdersAssigned == False:
        remainder = int(order.Number) % len(order.AvailabilityZones)
        eachOrderGets = int((int(order.Number) - remainder) /
                            len(order.AvailabilityZones))
        # here we assign all the orders
        for az in order.AvailabilityZones:
            az.Number = eachOrderGets
            if remainder != 0:
                az.Number += 1
                remainder -= 1

    # this client can be used for all the az's
    print(order.Region)
    client = boto3.client('ec2', region_name=order.Region,aws_access_key_id=order.aws_access_key_id,aws_secret_access_key=order.aws_secret_access_key)
    for az in order.AvailabilityZones:

        # for each AZ we're buying from
        kwargs = order.getKwargs(az.Name)
        response = client.describe_reserved_instances_offerings(**kwargs)
        ReservedInstancesOfferings = response["ReservedInstancesOfferings"]

        # we search for all instance types, not just fixed or hourly, then sort when we recieve results
        # do the sorting of the reserved instances by price, cheapest first
        allOfferings = []

        # get all the offerings objects
        for instanceOffering in ReservedInstancesOfferings:
            # isFixed and isHourly completely filter out or in whether or not those instance types get included
            # if both are true, then all types of instances get included regardless of payment type

            # for limits, 0 means no limit, everything else abides by the limit

            iOffering = getInstanceOffering(instanceOffering)
            fixedPrice = iOffering.FixedPrice
            recurringAmount = iOffering.RecurringAmount
            fixedPriceExists = False
            recurringAmountExists = False

            if fixedPrice is not None and fixedPrice != 0:
                fixedPriceExists = True
            if recurringAmount is not None and recurringAmount != 0:
                recurringAmountExists = True

            MaxFixedPrice = 0
            if order.MaxFixedPrice is not None:
                MaxFixedPrice = order.MaxFixedPrice

            MaxRecurringPrice = 0
            if order.MaxHourlyPrice is not None:
                MaxRecurringPrice = order.MaxHourlyPrice

            if order.isFixedPrice == True and order.isHourlyPrice == True:
                # either hourly or fixed or both
                if fixedPriceExists and recurringAmountExists:
                    if (MaxFixedPrice == 0 or iOffering.FixedPrice <= MaxFixedPrice) and (MaxRecurringPrice == 0 or iOffering.RecurringAmount <= MaxRecurringPrice):
                        allOfferings.append(iOffering)
                elif fixedPriceExists:
                    if MaxFixedPrice == 0 or iOffering.FixedPrice <= MaxFixedPrice:
                        allOfferings.append(iOffering)
                elif recurringAmountExists:
                    if MaxRecurringPrice == 0 or iOffering.RecurringAmount <= MaxRecurringPrice:
                        allOfferings.append(iOffering)

            elif order.isFixedPrice == True:
                # only fixed price servers
                if fixedPriceExists and recurringAmountExists == False:
                    if MaxFixedPrice == 0 or iOffering.FixedPrice <= MaxFixedPrice:
                        allOfferings.append(iOffering)

            elif order.isHourlyPrice == True:
                # only hourly servers
                if recurringAmountExists and fixedPriceExists == False:
                    if MaxRecurringPrice == 0 or iOffering.RecurringAmount <= MaxRecurringPrice:
                        allOfferings.append(iOffering)

        # sort into cost effectiveness, and these all have the correct AZ
        allOfferings.sort(key=lambda x: x.EffectiveHourlyRate)

        # print(order.Number)
        if order.Number is not None and order.Number > 0:
            if order.ordered is None:
                # brand new order bring it up to speed
                order.ordered = 0

            if az.ordered >= az.Number:
                print("AZ", az.Name, "has already been fulfilled with",
                      az.ordered, "instances")
            # buy until finished
            purchasedJustNow = 0
            previouslyPurchased = az.ordered
            for instanceOffering in allOfferings:
                # instanceOffering.print()
                # also we might want to write to the file, like keep it open, and update it for each order bought
                # something might go wrong
                # print(instanceOffering, "\n")
                if order.ordered < order.Number and az.ordered < az.Number:
                    # do purchase
                    order.ordered += 1
                    az.ordered += 1
                    purchasedJustNow += 1
                    instance = allOfferings.pop(0)
                    kwargs = instance.getKwargs(order.DryRun)
                    response = None
                    try:
                        response = client.purchase_reserved_instances_offering(
                            **kwargs)
                        print(response)
                    except:
                        pass
                    print("Just Purchased:")
                    instanceOffering.print()
                    order.PurchasedInstances.append(instanceOffering)

                if order.ordered >= order.Number or az.ordered >= az.Number:
                    break

            print(purchasedJustNow,
                  "Reserved Instances were just purchased for:", az.Name)
            print(previouslyPurchased, "instances had been purchased previously")
            if az.ordered >= az.Number:
                print("Purchased all", az.ordered,
                      "Reserved Instances for:", az.Name, "\n")
            else:
                print("Still need", int(az.Number - az.ordered), "instances for availability zone:",
                      az.Name, ", will attempt to purchase the rest during the next run", "\n")

    if order.ordered >= order.Number:
        print("Purchased all", order.ordered,
              "Reserved Instances for this order\n\n")
    else:
        print("Could only purchase", order.ordered,
              "Reserved Instances for this order, will attempt to purchase the rest at a later date.\n\n")
    return


# globals
home = str(Path.home())

# remove this later
if loadSamples:
    for f in listdir(home+"/awsPurchasing/sampleDataDontTouch"):
        thing = ""
        with open(home+"/awsPurchasing/sampleDataDontTouch/"+f, "r") as o:
            thing = o.read()
        with open(home+"/awsPurchasing/"+f, "w") as o:
            o.write(thing)
###

fileNames = []  # all the current orders
# check folder under ~/awsPurchasing
for f in listdir(home+"/awsPurchasing"):
    if(f.endswith(".json")):
        rename(home+"/awsPurchasing/"+f, home+"/awsPurchasing/"+f[:-5]+".data")

for f in listdir(home+"/awsPurchasing"):
    if(f.endswith(".data")):
        fileNames.insert(0, f)

# for each data file, load it, try to make an order,
for fi in fileNames:
    # find all the orders, parse them from input, attempt purchases
    with open(home+"/awsPurchasing/"+fi) as o:
        # read in the data file for this set of orders
        # and create some order objects
        # then try to purchase the instances as required
        # for idx, individualOrder in enumerate(json.load(o)):
        individualOrder = json.load(o)
        currentOrder = getNewOrder(individualOrder)

        # ATTEMPT PURCHASES FOR THIS ORDER
        attemptPurchases(currentOrder)

    # check if all the orders are complete
    finishedOrdering = True
    if currentOrder.ordered != currentOrder.Number:
        finishedOrdering = False

    # write all the data files to their original file
    with open(home+"/awsPurchasing/"+fi, "w") as o:
        o.write(json.dumps(currentOrder.getJson()))
    # if they are all complete
    if finishedOrdering:
        # move data file and order file to finished
        rename(home+"/awsPurchasing/"+fi, home+"/awsPurchasing/purchased/"+fi)
