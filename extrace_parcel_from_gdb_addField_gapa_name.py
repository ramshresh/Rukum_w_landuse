import arcpy, os
from arcpy import env

search = "Parcel"
workspace = "C:\GIS\landuse\Rukum"
outdir="C:\GIS\landuse\Rukum\parcels_shp_gapa_napa"
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
                         print "Add field GAPA_NAPA <String> and assign gbd_name as value"
                         # Add field GAPA_NAPA <String> and assign gbd_name as value
                         arcpy.AddField_management(in_table=fc_out, field_name="GAPA_NAPA", field_type="TEXT")
                         arcpy.CalculateField_management(in_table=fc_out,
                                field="GAPA_NAPA",
                                expression="'%s'" %(db_name),
                                expression_type="PYTHON_9.3" )                      
                         print "ok"
                         result.append(fc_out)         
    return result
fcs = get_fcs()

    
