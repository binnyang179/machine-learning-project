import tensorflow as tf
filenames = ["data/test_id_Aug_agg_private5k.csv", "data/UAI_sample_submission"]
record_defaults = [tf.float32] * 8   # Eight required float columns
dataset = tf.contrib.data.CsvDataset(filenames, record_defaults)
print(type(dataset))