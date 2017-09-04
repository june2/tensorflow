from operator import eq

class StringParser:
    def __init__(self):
        self.prepareData = []
        self.categoryArray = []
        self.xData = []
        self.yData = []
        self.isDebug = False


    def setString (self, arr):
        #self.originString = string.lower()
        #self.prepareData = self.originString.split('\n')        
        self.prepareData = arr

        if self.isDebug == True:
            print('=' * 100)
            print('prepare data : ')
            print(self.prepareData)
            print('=' * 100)

        #spaceLocation = self.originString.find(' ')


        #remove dummy 
        for tempString in self.prepareData:
            if len(tempString) < 1:
                self.prepareData.remove(tempString)
        #remove dummy end


        categoryArray = []        
        for tempString in self.prepareData:
            firstSpaceLocation = tempString.find(' ')
            currentCategoryString = tempString[0:firstSpaceLocation]

            firstSpaceLocation = tempString.find(' ')
            currentCategoryString = tempString[0:firstSpaceLocation]

            # Find category / Sort
            if len(categoryArray) == 0:
                categoryArray.append(currentCategoryString)
            else:
                isExistCategory = False
                for category in categoryArray:
                    if eq(category, currentCategoryString):
                        isExistCategory = True
                
                if isExistCategory == False:
                    categoryArray.append(currentCategoryString)
            # Find Category / Sort End

    
        self.categoryArray = categoryArray

        #log
        if self.isDebug == True:
            print('=' * 100)
            print('sorted category : ') 
            print(self.categoryArray)
            print('=' * 100)

    def getXData(self):
        # Make String Array ["asdfasdf asdf asdfasdfasdf", ...]
        returnArray = []
        for tempString in self.prepareData:
            firstSpaceLocation = tempString.find(' ')
            currentString = tempString[firstSpaceLocation+1 : len(tempString)].replace("\n", "").lower()
            returnArray.append(currentString)

        self.xData = returnArray

        if (self.isDebug == True):
            print('=' * 100)
            print('sorted category : ') 
            print(self.xData)
            print('=' * 100)

        return self.xData


    def getYData(self):
        # Make Category Index Array ex) [0, 0, 0, 1, 0, 0, 0, ...]
        returnArray = []
        category = []
        countCategory = 0;

        for tempString in self.prepareData:
           
            currentCategoryIndexArray = []            

            #get category string
            firstSpaceLocation = tempString.find(' ')
            currentCategoryString = tempString[0:firstSpaceLocation]
            currentCategoryIndex = self.categoryArray.index(currentCategoryString)
            
            if currentCategoryIndex >= len(category):
                category.append(currentCategoryString)                                           
            
            if (currentCategoryIndex > countCategory):
                countCategory = currentCategoryIndex
            
            if self.isDebug:
                print(currentCategoryIndexArray)

            returnArray.append([currentCategoryIndex])
            
        return category, returnArray
