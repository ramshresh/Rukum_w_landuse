import arcpy  
arcpy.env.workspace = r"C:\GIS\landuse\Rukum\parcels_shp_gapa_napa"  
fcs = arcpy.ListFeatureClasses()  
arcpy.Merge_management(fcs, r"C:\GIS\landuse\Rukum\parcels_merged_shp_gapa_napa\Rukum_Parcels_merged_all_gapa_napa.shp")  
