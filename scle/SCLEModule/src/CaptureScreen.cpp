//#include <windows.h>
//#include <string>
//#include <vector>
//#include <fstream>
//#include <cmath>
//#include <storm.h>
//#include "CaptureScreen.h"
//#include "base64.h"
//#include <BW/Offsets.h>
//
//namespace BW
//{
//  Bitmap::Bitmap(int width, int height, void *pBuffer)
//    : wid(static_cast<u16>(width))
//    , ht(static_cast<u16>(height))
//    , data(static_cast<u8*>(pBuffer != nullptr ? pBuffer : SMAlloc(width*height)))
//  {}
//
//  u8 *Bitmap::getData() const
//  {
//    if (this)
//      return this->data;
//    return nullptr;
//  }
//
//  int Bitmap::width() const
//  {
//    if (this)
//      return this->wid;
//    return 0;
//  }
//
//  int Bitmap::height() const
//  {
//    if (this)
//      return this->ht;
//    return 0;
//  }
//}
//
//std::string STORMAPI CaptureScreenToBase64() {
//
//  BW::Bitmap screenBuffer = BW::BWDATA::GameScreenBuffer;
//
//  int height = screenBuffer.height();
//  int width = screenBuffer.width();
//
//  int dataLength = height * width; // The screenbuffer data has one byte per pixel
//  
//  std::string base64screen = base64_encode(screenBuffer.getData(), dataLength);
//
//  
//  return base64screen;
//}
//
//BW::Bitmap screenBuffer = BW::BWDATA::GameScreenBuffer;
