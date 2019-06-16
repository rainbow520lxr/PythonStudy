import os
import tensorflow as tf

slim = tf.contrib.slim

FILE_PATTERN = 'fer2013_%s_*.tfrecord'

SPLITS_TO_SIZES = {
    'train': 1281167,
    'validation': 50000,
}

ITEMS_TO_DESCRIPTIONS = {
    'image': 'A color image of varying height and width.',
    'label': 'The label id of the image, integer between 0 and 6',
}


NUM_CLASSES = 7


def get_split(split_name, dataset_dir, file_pattern=None, reader=None):
    """Gets a dataset tuple with instructions for reading ImageNet.

    Args:
        split_name: A train/test split name.
        dataset_dir: The base directory of the dataset sources.
        file_pattern: The file pattern to use when matching the dataset sources.
            It is assumed that the pattern contains a '%s' string so that the split
            name can be inserted.
        reader: The TensorFlow reader type.

    Returns:
        A `Dataset` namedtuple.

    Raises:
        ValueError: if `split_name` is not a valid train/test split.
    """
    if split_name not in SPLITS_TO_SIZES:
        raise ValueError('split name %s was not recognized.' % split_name)

    if not file_pattern:
        file_pattern = FILE_PATTERN
    file_pattern = os.path.join(dataset_dir, file_pattern % split_name)

    # Allowing None in the signature so that dataset_factory can use the default.
    if reader is None:
        reader = tf.TFRecordReader

    keys_to_features = {
        'image/encoded': tf.FixedLenFeature((), tf.string, default_value=''),
        'image/format': tf.FixedLenFeature((), tf.string, default_value='jpeg'),
        'image/label': tf.FixedLenFeature((), tf.int64, default_value=0)
    }

    items_to_handlers = {
        'image': slim.tfexample_decoder.Image('image/encoded', 'image/format', channels=3),
        'label': slim.tfexample_decoder.Tensor('image/label'),
    }

    decoder = slim.tfexample_decoder.TFExampleDecoder(
            keys_to_features, items_to_handlers)

    return slim.dataset.Dataset(
            data_sources=file_pattern,
            reader=reader,
            decoder=decoder,
            num_samples=SPLITS_TO_SIZES[split_name],
            items_to_descriptions=ITEMS_TO_DESCRIPTIONS,
            num_classes=NUM_CLASSES)