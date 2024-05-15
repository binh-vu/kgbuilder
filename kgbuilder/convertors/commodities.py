from drepr.readers.prelude import read_source_csv
from drepr.writers.rdfgraph_writer import RDFGraphWriter

def main(resource_0):
	resource_data_1 = read_source_csv(resource_0)
	
	preprocess_0(resource_data_1)
	preprocess_1(resource_data_1)
	writer_16 = RDFGraphWriter({"mndr": "https://minmod.isi.edu/resource/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "owl": "http://www.w3.org/2002/07/owl#", "gkbi": "https://geokb.wikibase.cloud/entity/", "drepr": "https://purl.org/drepr/1.0/", "xsd": "http://www.w3.org/2001/XMLSchema#"})
	
	# Transform records of class mndr:Commodity:1
	start_17 = 1
	end_18 = len(resource_data_1)
	for minmod_id_index_0_19 in range(start_17, end_18):
		minmod_id_value_0_20 = resource_data_1[minmod_id_index_0_19]
		minmod_id_value_1_21 = minmod_id_value_0_20[0]
		writer_16.begin_record("https://minmod.isi.edu/resource/Commodity", minmod_id_value_1_21, False, False)
		
		# Retrieve value of data property: label
		label_index_0_22 = minmod_id_index_0_19
		label_value_0_23 = resource_data_1[label_index_0_22]
		label_value_1_24 = label_value_0_23[2]
		writer_16.write_data_property("http://www.w3.org/2000/01/rdf-schema#label", label_value_1_24, "http://www.w3.org/2001/XMLSchema#string")
		
		# Retrieve value of data property: name
		name_index_0_25 = minmod_id_index_0_19
		name_value_0_26 = resource_data_1[name_index_0_25]
		name_value_1_27 = name_value_0_26[2]
		writer_16.write_data_property("https://minmod.isi.edu/resource/name", name_value_1_27, "http://www.w3.org/2001/XMLSchema#string")
		
		# Retrieve value of data property: mrds
		mrds_index_0_28 = minmod_id_index_0_19
		mrds_value_0_29 = resource_data_1[mrds_index_0_28]
		mrds_value_1_30 = mrds_value_0_29[1]
		writer_16.write_data_property("https://minmod.isi.edu/resource/name_mrds", mrds_value_1_30, "http://www.w3.org/2001/XMLSchema#string")
		
		# Retrieve value of data property: sameAs
		sameAs_index_0_31 = minmod_id_index_0_19
		sameAs_value_0_32 = resource_data_1[sameAs_index_0_31]
		sameAs_value_1_33 = sameAs_value_0_32[3]
		writer_16.write_data_property("http://www.w3.org/2002/07/owl#sameAs", sameAs_value_1_33, "https://purl.org/drepr/1.0/uri")
		
		writer_16.end_record()
	
	output_34 = writer_16.write_to_string()
	return output_34

def preprocess_0(resource_data_2):
	start_4 = 1
	end_5 = len(resource_data_2)
	for preproc_0_path_index_0_6 in range(start_4, end_5):
		preproc_0_path_value_0_7 = resource_data_2[preproc_0_path_index_0_6]
		preproc_0_path_value_1_8 = preproc_0_path_value_0_7[3]
		preproc_0_path_value_0_7[3] = preproc_0_customfn(preproc_0_path_value_1_8)

def preproc_0_customfn(value):
	return "https://geokb.wikibase.cloud/entity/" + value


def preprocess_1(resource_data_9):
	start_11 = 1
	end_12 = len(resource_data_9)
	for preproc_1_path_index_0_13 in range(start_11, end_12):
		preproc_1_path_value_0_14 = resource_data_9[preproc_1_path_index_0_13]
		preproc_1_path_value_1_15 = preproc_1_path_value_0_14[0]
		preproc_1_path_value_0_14[0] = preproc_1_customfn(preproc_1_path_value_1_15)

def preproc_1_customfn(value):
	return "https://minmod.isi.edu/resource/" + value


if __name__ == "__main__":
	import sys
	
	print(main(*sys.argv[1:]))