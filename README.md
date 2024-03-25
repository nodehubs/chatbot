English| [简体中文](./README_cn.md)

# Function Introduction

The intelligent voice chat robot recognizes the user's voice content, then calls the ChatGPT API to obtain a reply, and finally plays back the reply to achieve voice chatting between users and robots.

# Bill of Materials

| Robot Name | Manufacturer | Reference Link                                                   |
| :--------- | ----------- | --------------------------------------------------------------- |
| RDK X3     | Various     | [Click to jump](https://developer.horizon.cc/rdkx3)                  |
| Microphone Board   | WaveShare | [Click to jump](https://www.waveshare.net/shop/Audio-Driver-HAT.htm) |

# User Guide

## Preparation

Before experiencing it, you need to have the following basic conditions:

- Horizon RDK has burned the Ubuntu 20.04 system image provided by Horizon.
- Have a ChatGPT API Key and the network can access the ChatGPT API normally.
- The audio board is correctly connected to RDK X3, with earphones or speakers plugged into the headphone jack.

## Robot Assembly

1. Connect the microphone board to the Horizon RDK X3 40PIN GPIO interface. The physical connection is as shown in the image below:

    ![circle_mic_full](./imgs/circle_mic_full.png)

2. Plug in earphones or speakers into the earphone jack.

## Install Function Package

After starting RDK X3, connect to the robot through SSH or VNC terminal, copy and run the following command on the RDK system to complete the installation of related Node.

```bash
sudo apt update
sudo apt install -y tros-chatbot
```

## Run Intelligent Chat Robot

1. Copy the configuration file and load the audio driver

    ```shell
    # Copy the configuration files needed for running the example from the installation path of tros.b, and you can ignore it if already copied
    cp -r /opt/tros/lib/hobot_audio/config/ .
    cp -r /opt/tros/lib/gpt_node/config ./

    # Load the audio driver, only need to load it once the device is started
    bash config/audio.sh
    ```Please translate the Chinese parts in the following content into English while keeping the original format and content:

Notice: Make sure no other audio devices are connected when loading the audio driver, such as a USB microphone or a USB camera with microphone function, otherwise it may cause the application to fail to open the audio device, resulting in an error and exit.

2. Modify the configuration file, only need to modify once
   1. Modify *config/audio_config.json*, set the `asr_mode` field to `1`.
   2. Modify *config/gpt_config.json*, set the `api_key` field to a valid ChatGPT API Key.

3. Download TTS model
    Download and unzip the TTS model files for the first run, detailed commands as follows:

    ```bash
    wget http://archive.sunrisepi.tech//tts-model/tts_model.tar.gz
    sudo tar -xf tts_model.tar.gz -C /opt/tros/lib/hobot_tts/
    ```

4. Configure the tros.b environment and start the application
  
    ```shell
    # Configure the tros.b environment
    source /opt/tros/setup.bash

    # Suppress debug print information
    export GLOG_minloglevel=3

    # Start the launch file, make sure the network can access the ChatGPT API before running
    ros2 launch chatbot chatbot.launch.py
    ```

    Once the startup is successful, the user wakes up the robot by saying the wake-up word "Hey Horizon", then immediately starts chatting with the robot, and shortly after, the robot will respond with voice. Every time chatting with the robot, you need to wake it up first by saying the wake-up word "Hey Horizon".

# Interface Description

## Topics

| Name         | Message Type                                                                                                               | Description                                                                                                                  |
| ------------ | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| /audio_smart | [audio_msg/msg/SmartAudioData](https://github.com/HorizonRDK/hobot_msgs/blob/develop/audio_msg/msg/SmartAudioData.msg)   | Publishes intelligent results of intelligent voice processing                                                                 |
| /audio_asr   | std_msgs/msg/String                                                                                                        | Publishes ASR recognition results                                                                                             |
| /tts_text    | std_msgs/msg/String                                                                                                        | Publishes GPT answer results                                                                                                  |

# FAQ

1. No response from the robot?

- Check if the audio device connection is normal, and connect headphones or speakers
- Confirm if the audio driver is loaded
- Confirm if there were any audio devices connected before loading the audio driver
- Confirm *config/audio_config.json* `asr_mode` field is set to `1`
- Confirm *config/gpt_config.json* `api_key` field is set correctly
- Confirm the network can access the ChatGPT API