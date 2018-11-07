from __future__ import print_function
import numpy as np
import tensorflow as tf

import argparse, time, os, boto3, boto3.session
from six.moves import cPickle

from utils import TextLoader
from model import Model

def main():
    #this was just canibalized from when there used to be commandline inputs for this script. it's not clean but it works
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, default=34,
                       help='number of words to sample')
    parser.add_argument('--prime', type=str, default=' ',
                       help='prime text')
    parser.add_argument('--pick', type=int, default=1,
                       help='1 = weighted pick, 2 = beam search pick')
    parser.add_argument('--width', type=int, default=4,
                       help='width of the beam search')
    parser.add_argument('--sample', type=int, default=1,
                       help='0 to use max at each timestep, 1 to sample at each timestep, 2 to sample on spaces')
    parser.add_argument('--count', '-c', type=int, default=1,
                       help='number of samples to print')
    parser.add_argument('--quiet', '-q', default=True, action='store_true',
                       help='suppress printing the prime text (default was false, I changed it to true)')
    args = parser.parse_args()
    return args

def sample(args):
    #boto connecting to S3 bucket
    client = boto3.client('s3')
    obj_test = client.get_object(Bucket='zappa-hziu2pf5g', Key='save/config.pkl')
    words = client.get_object(Bucket='zappa-hziu2pf5g', Key='save/words_vocab.pkl')
    vocab = client.get_object(Bucket='zappa-hziu2pf5g', Key='save/words_vocab.pkl')
    checkpoint = client.get_object(Bucket='zappa-hziu2pf5g', Key='save/')

    #read in file from the boto connection
    #checkpoint_string = checkpoint['Body'].read()
    body_string = obj_test['Body'].read()

    saved_args = cPickle.loads(body_string)
    model = Model(saved_args, False) #boolean is for 'infer'
    output = ''
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        #saver = tf.train.Saver(tf.global_variables())
        #print('global variables initialized and saved')

        #this is where it gets hairy, chekpoint_state wants a directory
        #ckpt = tf.train.get_checkpoint_state(checkpoint)
        #print('checkpoint data reached before if statement')
        #I believe restore wants two arguments but I may be wrong
        #if ckpt and ckpt.model_checkpoint_path:
            #saver.restore(sess, checkpoint_string, ckpt.model_checkpoint_path)
            #print('passed checkpoint data successfully')
        try:
            output = model.sample(sess, words, vocab, args.n, args.prime, args.sample, args.pick, args.width, args.quiet)
        except:
            print('the try variable assignment failed')
    return output

if __name__ == '__main__':
    main()
