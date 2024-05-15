from drepr.readers.prelude import read_source_csv
from drepr.writers.rdfgraph_writer import RDFGraphWriter

def main(resource_0):
	resource_data_1 = read_source_csv(resource_0)
	
	writer_2 = RDFGraphWriter({"mndr": "https://minmod.isi.edu/resource/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "owl": "http://www.w3.org/2002/07/owl#", "drepr": "https://purl.org/drepr/1.0/", "xsd": "http://www.w3.org/2001/XMLSchema#"})
	
	# Transform records of class mndr:MineralSite:1
	start_3 = 1
	end_4 = len(resource_data_1)
	for minmod_id_index_0_5 in range(start_3, end_4):
		minmod_id_value_0_6 = resource_data_1[minmod_id_index_0_5]
		minmod_id_value_1_7 = minmod_id_value_0_6[0]
		writer_2.begin_record("https://minmod.isi.edu/resource/MineralSite", minmod_id_value_1_7, False, False)
		
		# Retrieve value of data property: same_as_id
		same_as_id_index_0_8 = minmod_id_index_0_5
		same_as_id_value_0_9 = resource_data_1[same_as_id_index_0_8]
		same_as_id_value_1_10 = same_as_id_value_0_9[1]
		writer_2.write_data_property("http://www.w3.org/2002/07/owl#sameAs", same_as_id_value_1_10, "https://purl.org/drepr/1.0/uri")
		
		writer_2.end_record()
	
	output_11 = writer_2.write_to_string()
	return output_11

if __name__ == "__main__":
	import sys
	
	print(main(*sys.argv[1:]))