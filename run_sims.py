# Simple script that runs all working run configurations via loop 
# and creates local directories for trace outputs with labels for organization
# Currently only loops through schedulers (not topologies) because it's suspected that
# further settings need to be adjusted to run custom data center topology configs
# (see todo below about setup_params.tcl)

import os


schedulers = ("Green", "RoundRobin", "Random", "HEROS", "RandDENS", "BestDENS")
											    # NCore NAggr NAccess NRackHosts
topologies = ("three-tier\ debug", 				# 1 3 48 	
			  "three-tier\ heterogenous\ debug",  # 1 3 48		  
			  "three-tier\ high-speed", 			# 2 2*NCore 256 3 
			  "default" 						# 8 64 3
			  # "small_dc", 					# 1 3 48
 			  # "full_scale_dc"				    # 8 64 3
			  # "three-tier"  # ask about this
 			  )


#deadline = ()
#trace_out_dirs = ()
#task_types = ()
trace_local_dir = ""

# todo: figure out fully configuration details of topologies (non default configs in various .tcl files such as  setup_params.tcl) then add to loop			  

# run config with schedulers
for scheduler_name in schedulers:
	for top_name in topologies:	
		print("------------------------------------------------------------\n\n\n\n\n")
		print("Now running simulation for: " + scheduler_name + " scheduler with " + top_name + " topology") 
		print("\n\n\n\n\n------------------------------------------------------------")
		# creating local trace dir for organization - also stops deletion due to unique dir
		trace_local_dir = scheduler_name + "-" + top_name
	
		# runs config in terminal
		os.system("./run" + 
				  " --topology=" + top_name +
				  " --scheduler=" + scheduler_name +
				  " --trace-dir=/traces/" + trace_local_dir +
				  " --clean-old=false"
				  )
			  
			  
			  
# todo: once dc topology figured out, can add portions of the following to the loop 
#print("\n\nNow running simulation for: " + schedulers[0] + " scheduler\n\n")
#os.system("echo Now running simulation for the " + scheduler + " scheduler")
#trace_local_dir = schedulers[0] + "_" + topologies[-1]

#os.system("./run " +
#			  "--topology=three-tier" +
#			  "--scheduler=" + schedulers[0] 
#			  + " --trace-dir=/traces/" + trace_local_dir
			  # add in trace file paths next
#			  )
