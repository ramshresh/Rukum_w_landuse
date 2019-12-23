import arcpy, os
from arcpy import env

search = "Parcel"
workspace = "D:\Rukum"
outdir="D:\Rukum\parcels_shp"
def get_geodatabase_path(input_table):
  '''Return the Geodatabase path from the input table or feature class.
  :param input_table: path to the input table or feature class 
  '''
  workspace = os.path.dirname(input_table)
  if [any(ext) for ext in ('.gdb', '.mdb', '.sde') if ext in os.path.splitext(workspace)]:
    return workspace
  else:
    return os.path.dirname(workspace)

def get_fcs():    
    fcs = []
    walk = arcpy.da.Walk(workspace, datatype="FeatureClass")
    result = []
    for dirpath, dirnames, filenames in walk:
        item = {}
        for filename in filenames:
            #print filenames
            if search == filename:
                         fc_in = os.path.join(dirpath, filename)
                         db_name = os.path.splitext(os.path.basename(get_geodatabase_path(fc_in)))[0]
                         shp_name = search+"_"+db_name.replace('-','')+".shp"
                         fc_out=os.path.join(outdir, shp_name)
                         print "CopyFeatures "+fc_out
                         arcpy.CopyFeatures_management(fc_in, fc_out)
                         print "ok"
                         result.append(fc_out)         
    return result
fcs = get_fcs()

    
