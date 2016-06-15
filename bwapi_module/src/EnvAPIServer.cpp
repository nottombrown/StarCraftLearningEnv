#include <zmq.hpp>  // zmq must be included first, otherwise it will conflict with the windows socket library
#include "EnvAPIServer.h"
#include <tuple>
#include <string>
#include <map>
#include <json.h>
#include <iostream>
#include "CaptureScreen.h"

#ifndef _WIN32
#include <unistd.h>
#else

#include <windows.h>
#define sleep(n)    Sleep(n)
#endif

//  Prepare our context and socket
zmq::context_t context(1);
zmq::socket_t zmqSocket(context, ZMQ_REP);


namespace EnvAPIServer{
  //------------------------------------------------ MOUSE/KEY INPUT -----------------------------------------
  void pressKey(int key)
  {
    // Don't do anything if key is 0
    // used when auto-menu dialogs are not found, performance
    if (!key)
      return;

    // Press and release the key
    PostMessage(SDrawGetFrameWindow(), WM_CHAR, (WPARAM)key, NULL);
    std::string message;
    message = "Pressed key: " + std::to_string(key);
  }

  void mouseDown(int x, int y)
  {
    // Press the left mouse button
    PostMessage(SDrawGetFrameWindow(), WM_LBUTTONDOWN, NULL, (LPARAM)MAKELONG(x, y));
  }

  void mouseUp(int x, int y)
  {
    // Release the left mouse button
    PostMessage(SDrawGetFrameWindow(), WM_LBUTTONUP, NULL, (LPARAM)MAKELONG(x, y));
  }



  //------------------------------------------------ REQUEST HANDLERS -----------------------------------------


  void handleActionCommand(Json::Value data) {

    //Broodwar->sendText(actionData.asCString());
    BWAPI::Broodwar->sendText("Handling action");
    if (data.isMember("mouse")){
      mouseUp(data["mouse"]["x"].asInt(), data["mouse"]["y"].asInt());
    }

    //pressKey(1);

  }


  //------------------------------------------------ SERVER METHODS -----------------------------------------



  std::string receiveMessagePart() {
    // Receive a single zmq::message_t and convert it to a std::string
    zmq::message_t request;
    zmqSocket.recv(&request);
    std::string requestStr = std::string(static_cast<char*>(request.data()), request.size());
    return requestStr;
  }


  void bind() {
    zmqSocket.bind("tcp://*:80");
  }

  void listen() {
    return;
    
    //  Wait for next request from client
    std::string requestEndpoint = receiveMessagePart();
    std::string requestHeadersJSON = receiveMessagePart();
    std::string requestBodyJSON = receiveMessagePart();

    BWAPI::Broodwar->sendText(requestEndpoint.c_str());
    BWAPI::Broodwar->sendText(requestHeadersJSON.c_str());
    BWAPI::Broodwar->sendText(requestBodyJSON.c_str());

    Json::Value requestRoot;
    Json::Reader reader;
    bool parsingSuccessful = reader.parse(requestBodyJSON, requestRoot);

    if (!parsingSuccessful) {
      BWAPI::Broodwar->sendText("Failed to parse command from client");
    }
    else {
      //std::string command = requestRoot["command"].asString();

      //if (command == "step") {
      //  handleActionCommand(requestRoot["data"]);
      //}
      //else if (command == "reset") {

      //}
      //else if (command == "configure") {

      //}
    }

    //  Send reply back to client
    Json::Value responseRoot;
    zmq::message_t reply(5);
    memcpy(reply.data(), "state", 5);
    zmqSocket.send(reply, ZMQ_SNDMORE);
  }
}
