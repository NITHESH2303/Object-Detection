"""
frame_num = int((cv2.CAP_PROP_FRAME_COUNT))
frame_width = int((cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int((cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('out_video.mp4', fourcc, 30, frame_width, frame_height)
out.write(img)

frame_exists, curr_frame = capture.read()
if frame_exists:
    print("for frame : " + str(frame_no) + "   timestamp is: ", str(capture.get(cv2.CAP_PROP_POS_MSEC)))
else:
    break
frame_no += 1
cv2.imshow('video', img)

key = cv2.waitKey(1)
    if key == 27:
        break
# print('obj'+count,'time'+timestamp)
capture.release()

cv2.destroyAllWindows()
"""