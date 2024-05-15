from drepr.readers.prelude import read_source_csv
from drepr.writers.rdfgraph_writer import RDFGraphWriter

def main(resource_0):
	resource_data_1 = read_source_csv(resource_0)
	
	preprocess_0(resource_data_1)
	writer_9 = RDFGraphWriter({"mndr": "https://minmod.isi.edu/resource/", "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "owl": "http://www.w3.org/2002/07/owl#", "gkbi": "https://geokb.wikibase.cloud/entity/", "drepr": "https://purl.org/drepr/1.0/", "xsd": "http://www.w3.org/2001/XMLSchema#"})
	
	# Transform records of class mndr:DepositType:1
	start_10 = 1
	end_11 = len(resource_data_1)
	for depid_index_0_12 in range(start_10, end_11):
		depid_value_0_13 = resource_data_1[depid_index_0_12]
		depid_value_1_14 = depid_value_0_13[1]
		writer_9.begin_record("https://minmod.isi.edu/resource/DepositType", depid_value_1_14, False, False)
		
		# Retrieve value of data property: label
		label_index_0_15 = depid_index_0_12
		label_value_0_16 = resource_data_1[label_index_0_15]
		label_value_1_17 = label_value_0_16[0]
		writer_9.write_data_property("http://www.w3.org/2000/01/rdf-schema#label", label_value_1_17, "http://www.w3.org/2001/XMLSchema#string")
		
		# Retrieve value of data property: name
		name_index_0_18 = depid_index_0_12
		name_value_0_19 = resource_data_1[name_index_0_18]
		name_value_1_20 = name_value_0_19[0]
		writer_9.write_data_property("https://minmod.isi.edu/resource/name", name_value_1_20, "http://www.w3.org/2001/XMLSchema#string")
		
		# Retrieve value of data property: env
		env_index_0_21 = depid_index_0_12
		env_value_0_22 = resource_data_1[env_index_0_21]
		env_value_1_23 = env_value_0_22[2]
		writer_9.write_data_property("https://minmod.isi.edu/resource/environment", env_value_1_23, "http://www.w3.org/2001/XMLSchema#string")
		
		# Retrieve value of data property: group
		group_index_0_24 = depid_index_0_12
		group_value_0_25 = resource_data_1[group_index_0_24]
		group_value_1_26 = group_value_0_25[3]
		writer_9.write_data_property("https://minmod.isi.edu/resource/deposit_group", group_value_1_26, "http://www.w3.org/2001/XMLSchema#string")
		
		# Retrieve value of data property: depid
		writer_9.write_data_property("https://minmod.isi.edu/resource/id", depid_value_1_14, "https://purl.org/drepr/1.0/uri")
		
		writer_9.end_record()
	
	output_27 = writer_9.write_to_string()
	return output_27

def preprocess_0(resource_data_2):
	start_4 = 1
	end_5 = len(resource_data_2)
	for preproc_0_path_index_0_6 in range(start_4, end_5):
		preproc_0_path_value_0_7 = resource_data_2[preproc_0_path_index_0_6]
		preproc_0_path_value_1_8 = preproc_0_path_value_0_7[1]
		preproc_0_path_value_0_7[1] = preproc_0_customfn(preproc_0_path_value_1_8)

def preproc_0_customfn(value):
	return "https://minmod.isi.edu/resource/" + value


if __name__ == "__main__":
	import sys
	
	print(main(*sys.argv[1:]))