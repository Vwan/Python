import numpy as np
import pandas as pd
from matplotlib import pyplot as plot
from matplotlib.backends.backend_pdf import PdfPages
import datetime as dt
from tkinter import filedialog
from os import path

def main():
	def createPDFlabels(labelData, savepath, name='defaultName.pdf', customField=True):
	    """
	    Create multipage PDFs of labels from label data
	    """
	    # The PDF document
	    saveOutput = path.join(savepath, name)
	    pdf_pages = PdfPages(saveOutput)

	    descriptions = {'month 1':'Watercolor paper(3), Watercolor pencils(12), Pencil(1), Fan brush(1), Eraser(1), Table cover(1), Stickers(2), Notebook(2), Pencil sharpener(1)',
	        'month 2':'Tote bag(1), Acrylic paint(3), Acrylic brush(2), Marker(1), Paint palette(1), Stickers(2), Coloring sheets(3), Sponges(3), Manila Paper(2), Watercolor paper(2)',
	        'month 3':'Oil pastel set(1), Chalk pastel set(1), Pencil crayon set(1), Multimedia paper(2), Manila paper(2), Washi tape(1), Pencil(1), Eraser(1), Microfiber towel(1)',
	        'month 4':'Construction Paper(1), Pipecleaners(3), Glitter Glue(1), Glue(1), Cardstock Paper(1), Neon Acrylic Paint(1), Eye Dropper(1), Paint Pallete(1), Watercolor Paper(1), Wide Brush(1), Liquid Watercolor(1)'}

	    for i in range(labelData.shape[0]):
	               
	        # This is what is going on each page
	        toText = 'To:'
	        addressText = ''
	        toCompany = labelData['ship to - company'][i]
	        toName = labelData['ship to - name'][i]
	        toAddress1 = labelData['ship to - address 1'][i]
	        toAddress2 = labelData['ship to - address 2'][i]
	        toAddress3 = labelData['ship to - address 3'][i]
	        toCity = labelData['ship to - city'][i]
	        toProvince = labelData['ship to - state'][i]
	        toPostalCode = labelData['ship to - postal code'][i]
	        toCountry = labelData['ship to - country'][i]

	
	        if pd.isnull(labelData['custom - field 1'][i]):
	        	description = 'No description Information'
	        	weight = 'unknown'
	        	value = 'unknown'
	        elif (labelData['custom - field 1'][i]).lower() in descriptions:
	            description = descriptions[(labelData['custom - field 1'][i]).lower()]
	            weight = '0.8'
	            value = '20.00'
	        else:
	            description = labelData['custom - field 1'][i]
	            weight = '0.8'
	            value = '20.00'

	        # Make sure that all the necessary information is there (Name)
	        if pd.isnull(toName):
	            raise ValueError('Customer {} of {} is missing name'.format(i, name))
	        if pd.isnull(toAddress1):
	            raise ValueError('Customer {} of {} is missing Address 1'.format(toName, name))
	        if pd.isnull(toCity):
	            raise ValueError('Customer {} of {} is missing City'.format(toName, name))
	        if pd.isnull(toCountry):
	            raise ValueError('Customer {} of {} is missing Country'.format(toName, name))

	        if pd.isnull(toProvince):
	            addressTextEnd = str(toCity) + ', ' + str(toCountry) + '\n' + str(toPostalCode)
	        if pd.notnull(toProvince):
	            addressTextEnd = str(toCity) + ', ' + str(toProvince) + ', ' + str(toCountry) + '\n' + str(toPostalCode)

	        if pd.notnull(toCompany):
	            addressText = addressText + '\n' + str(toCompany)
	        if pd.notnull(toName):
	            addressText = addressText + '\n' + str(toName)
	        if pd.notnull(toAddress1):
	            addressText = addressText + '\n' + str(toAddress1)
	        if pd.notnull(toAddress2):
	            addressText = addressText + '\n' + str(toAddress2)
	        if pd.notnull(toAddress3):
	            addressText = addressText + '\n' + str(toAddress3)

	        fullText = toText + '\n' + addressText + '\n' + addressTextEnd

	        a, (b, c) = plot.subplots(2,1, figsize=(4, 6))
	        a.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
	        b.axis('off')
	        c.axis('off')
	        b.text(.1, 0.35, 'From:\nShip Ninja \nc/o Think With Art \n113 Lampton Crescent \nMarkham, ON, Canada \nL6E 1N2')
	        b.text(.1, -.15, fullText)

	        # Include Custon Field 1 for manual orders
	        if customField:
	        	if pd.notnull(labelData['custom - field 1'][i]):
	        		manualText = labelData['custom - field 1'][i]
	        	else:
	        		manualText = 'No description Information'
	        	b.text(0.1, .75, 'Order: \n'+ manualText, fontsize=8)
	        	# elif pd.notnull(labelData)
	        
	        # Check to see if there's a gift message
	        if 'GIFT' in str(labelData['notes - from buyer'][i]):
	            giftMsg = str(labelData['notes - from buyer'][i]).split(': True\n\n', 1)[-1]
	            #force the gift message to have less that 50 Chars per line
	            tempText = giftMsg.split(' ', )
	            tmpText=''
	            characterLimit = 50
	            for i in range(len(tempText)):
	                if len(tmpText.split('\n')[-1] + tempText[i]) > characterLimit:
	                    tmpText = tmpText + '\n'
	                tmpText = tmpText + tempText[i] + ' '
	            b.text(.065, -0.25, tmpText)

	        # Insert CN22 Declaration for international packages
	        if toCountry != 'CA':
	            img = plot.imread("CN22.png")
	            c.imshow(img,zorder=0, aspect='equal')
	            descriptionSplit = description.split(' ')
	            tempDesc = ''
	            descLim = 40
	            for i in range(len(descriptionSplit)):
	                if len(tempDesc.split('\n')[-1] + descriptionSplit[i]) > descLim:
	                    tempDesc = tempDesc + '\n'
	                tempDesc = tempDesc + descriptionSplit[i] + ' '
	            c.text(340, 0, tempDesc, fontsize=6)
	            c.text(380, 160, weight, fontsize=8)
	            c.text(500, 160, value, fontsize=8)
	            c.text(450, 280, dt.datetime.today().strftime("%b-%d-%Y"), fontsize=8)
	        
	        # Done with the page
	        pdf_pages.savefig(a, dpi=150)
	        plot.close(a)

	    # Write the PDF document to the disk
	    pdf_pages.close()

	def boxCycles(boxData, savepath, name='Box Data', numCycles=4):
	    """
	    Creates PDF label package for each cycle in data
	    Input:
	    boxData: pandas dataframe of customer data for boxes including all cycles
	    numCycles: how many cycles should the program look at?
	    Output:
	    A pdf of labels for each cycle
	    """
	    for j in range(1, numCycles+1):
	        temp = boxData[boxData['custom - field 1'] == 'Month {}'.format(j)].reset_index(drop=True)
	        createPDFlabels(temp, savepath=savepath, name='{} Cycle {}.pdf'.format(name, j))

	def createAllPDFs():
	    """
	    Split that data so good and then run each section
	    through the label-making program, createPDFlabels
	    or through the boxCycle program for the box data.
	    """
	    # Which file should we use?
	    filepath = filedialog.askopenfile()
	    savepath = filedialog.askdirectory()
	    data = pd.read_csv(filepath.name)

	    # Lowercase all the columns to avoid mistakes
	    data.columns = data.columns.str.lower()
	    
	    # Eliminate any rows that have the Tag: 'Dont Ship'
	    if 'Dont Ship' in data['tags']:
	    	data = data[data['tags'] != 'Dont Ship'].reset_index(drop=True)
	    
	    # Fix UM --> US Country Code error
	    for i in range(data.shape[0]):
	        if data['ship to - country'][i] == 'UM':
	            data['ship to - country'][i] = 'US'
	    
	    manual = data[data['market - store name'] == 'Manual Orders'].reset_index(drop=True)
	    nonManual = data[data['market - store name'] != 'Manual Orders'].reset_index(drop=True)
	    
	    # USdata = nonManual[nonManual['ship to - country'] == 'US'].reset_index(drop=True)
	    NonUSdata = nonManual[nonManual['ship to - country'] != 'US'].reset_index(drop=True)
	    
	    ## Uncomment the following code to produce the US labels
	    # USmanual = manual[manual['ship to - country'] == 'US'].reset_index(drop=True)
	    # createPDFlabels(USmanual, savepath=savepath, name='US Manual.pdf')
	    # USboxes = USdata[USdata['amount - order shipping'] == 0].reset_index(drop=True)
	    # boxCycles(USboxes, savepath=savepath, name='US Boxes')
	    # USadapters = USdata[USdata['amount - order shipping'] > 0].reset_index(drop=True)
	    # createPDFlabels(USadapters, savepath=savepath, name='US Adapters.pdf')
	    
	    NonUSmanual = manual[manual['ship to - country'] != 'US'].reset_index(drop=True)
	    print(NonUSmanual.shape)
	    createPDFlabels(NonUSmanual, savepath=savepath, name='Non-US Manual.pdf')
	    NonUSboxes = NonUSdata.reset_index(drop=True)
	    boxCycles(NonUSboxes, savepath=savepath, name='Non-US Boxes')
	createAllPDFs()

if __name__ == '__main__':
	main()