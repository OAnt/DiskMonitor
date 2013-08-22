import web
from web import form
import DiskMonitor as DM
from Data import *
import GeneralFunctions as GF
import json
import os.path

#print DM

RadioListAnalysis=[]
RadioListDisc=[]
RadioUnit=[]

for Item in AnalysisDict.keys():
	RadioListAnalysis.append(Item)

for Item in DiscFuncDict.keys():
	RadioListDisc.append(Item)

for Item in UnitDict.keys():
	RadioUnit.append(Item.upper())
	
RadioUnit = sorted(RadioUnit, key = lambda Item: UnitDict[Item.lower()])
	
urls = (
	'/', 'index',
	'/loading','loading',
	'/result','result',
)


render = web.template.render('templates/')

Inputs = form.Form(
	form.Textbox('Path',
		value = 'Path'
		),
	form.Textbox('size',
		value = '100'
		),
	form.Radio('Unit',RadioUnit,
		value = 'MB'
		),
	form.Radio('Analysis',RadioListAnalysis,
		value = 'directorysizeordering'),
	form.Radio('Discrimination function', RadioListDisc,
		value = "pareto"),
)



class index:
	def GET(self):
		form = Inputs()
		return render.index(form, HelpContext)
	
	def POST(self):
		form = Inputs()
		if not form.validates():
			return render.index(form, HelpContext)
		else:
			#print form.d.Path, form['Analysis'].value, form['Discrimination function'].value, form['size'].value, form['Unit'].value
			try:
			
				if form['Discrimination function'].value == "limitsize":
					IntSize = int(form['size'].value)
				else:
					IntSize = 0
				
				if os.path.isdir(form.d.Path):
					#print RadioUnit
					#print form.d.Path
					FinalQuantity, FileQuantity, EndSize, TotalSize, EndList, Ending, Files, Skipt = DM.disk_monitor(
						form.d.Path.encode('latin-1'), 
						form['Analysis'].value, 
						form['Discrimination function'].value, 
						IntSize, 
						form['Unit'].value.lower()
						)
					
					#print FinalQuantity, FileQuantity, EndSize, TotalSize, EndList
					NewEndSize = GF.conversion_soft(EndSize)
					NewTotalSize = GF.conversion_soft(TotalSize)
					
					#print NewEndSize, NewTotalSize
					StrEndList = []
	
					for Item in EndList:
						TempSize = GF.conversion_soft(Item[1])
						aaa = Item[0]
						#print aaa
						TempStr = '<p><a href="file:///{0}">{0}</a>, Size: {1}</p>' .format(aaa,TempSize)
					
						StrEndList.append(TempStr)
					
					#StrEnd = "".join(StrEndList)
					#print StrEndList
					#print StrEnd
					
					#zzz = json.dumps(StrEndList)
			
					#print json.loads(zzz)
					return render.result(
						FinalQuantity, 
						FileQuantity, 
						NewEndSize, 
						NewTotalSize, 
						StrEndList,
						Ending,
						Files,
						Skipt
						)
						
				else:
					return render.index(form, HelpContext)
				
			except ValueError as e:
				print e
				return render.index(form, HelpContext)

				
if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()