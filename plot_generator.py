import matplotlib.pyplot as plt
import numpy as np
import boto3
import os

os.environ['MPLCONFIGDIR'] = '/tmp/matplotlib'

def upload_to_s3(file_path, bucket_name, object_name=None):
    s3_client = boto3.client('s3')
    if object_name is None:
        object_name = os.path.basename(file_path)
    
    try:
        response = s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"Successfully uploaded {file_path} to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")

def main():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    print("Plotting the sine wave...")

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Sine wave', color='blue')

    plt.title('Sine Wave Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()

    plot_path = '/tmp/sine_wave_plot.png'
    plt.savefig(plot_path)

    bucket_name = 'wcbuckt'
    upload_to_s3(plot_path, bucket_name)

    print("Plot saved and uploaded to S3.")

if __name__ == '__main__':
    main()
