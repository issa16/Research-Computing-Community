import tensorflow as tf

tf.config.threading.set_inter_op_parallelism_threads()
tf.config.threading.set_intra_op_parallelism_threads()
tf.config.set_soft_device_placement(True)

print('*' * 80)
num_threads = tf.config.threading.get_inter_op_parallelism_threads()
print(f'Num threads: {num_threads}')

print('*' * 80)
logical_devices = tf.config.list_logical_devices('CPU')
print(f'Logical Num CPUs: {len(logical_devices)}')
for devices in logical_devices:
    print(devices)

print('*' * 80)
physical_devices = tf.config.list_physical_devices('CPU')
print(f'Physical Num CPUs: {len(logical_devices)}')
for devices in physical_devices:
    print(devices)
