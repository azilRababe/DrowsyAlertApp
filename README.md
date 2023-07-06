# Drowsy Alert App

The Drowsy Alert App is a Python-based application that uses computer vision techniques to detect drowsiness in drivers. It utilizes facial landmarks and eye aspect ratio (EAR) to determine if a person's eyes are closed for an extended period, indicating drowsiness. When drowsiness is detected, the app provides an alert to help prevent accidents caused by driver fatigue.

## Features

- Real-time drowsiness detection using a webcam
- Eye tracking and EAR calculation for drowsiness assessment
- Alert system (sound alert and visual alert on the screen) when drowsiness is detected
- Configurable drowsiness threshold for personalized sensitivity

## Prerequisites

Before running the Drowsy Alert App, ensure that you have the following prerequisites installed:

- Python (version 3.6 or later)
- OpenCV (version 4.2.0 or later)
- dlib (version 19.18.0 or later)
- NumPy (version 1.20.0 or later)
- Playsound (version 1.2.2 or later)

You can install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

```
git clone https://github.com/azilRababe/DrowsyAlertApp.git
```

2. Navigate to the project directory:

```
cd DrowsyAlertApp
```

3. Run the application:

```
python app.py
```

4. Adjust the drowsiness threshold (optional):
   - Open the `app.py` file in a text editor.
   - Look for the `THRESHOLD` variable at the top of the file.
   - Modify the value to adjust the sensitivity of drowsiness detection. Higher values make it more sensitive, while lower values make it less sensitive.

## Troubleshooting

- If you encounter errors related to missing dependencies, ensure that you have installed the prerequisites correctly.
- Make sure your webcam is connected and functioning properly.
- If the eye detection or facial landmarks are not accurate, try adjusting the lighting conditions or positioning of your face in front of the camera.

## Contributing

Contributions to the DrowsyAlertApp project are welcome. If you find any issues or have suggestions for improvements, please open an issue on the [GitHub repository](https://github.com/azilRababe/DrowsyAlertApp/issues).

## Acknowledgements

The Drowsy Alert App is built upon various open-source libraries and resources. The following resources have been used in the development of this project:

- [OpenCV](https://opencv.org/)
- [dlib](http://dlib.net/)
- [Playsound](https://pypi.org/project/playsound/)

Special thanks to the contributors of these libraries and the open-source community for their valuable contributions.

## Disclaimer

The Drowsy Alert App is an educational project and should not be solely relied upon for ensuring road safety.
