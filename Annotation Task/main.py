import cv2

cropping = False

x_start, y_start, x_end, y_end = 0, 0, 0, 0


image = cv2.imread('Task_1.jpg')
oriImage = image.copy()


def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping

    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True

    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            x_end, y_end = x, y

    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False  # cropping is finished

        refPoint = [(x_start, y_start), (x_end, y_end)]

        if len(refPoint) == 2:  # when two points were found
            Task_1_cropped = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped", Task_1_cropped)
            cv2.imwrite('Task_1_Cropped.jpg', Task_1_cropped)


cv2.namedWindow("image", 2)
cv2.setMouseCallback("image", mouse_crop)

while True:

    Task_1_insights = image.copy()

    if not cropping:
        cv2.imshow("image", image)

    elif cropping:
        Task_1_insights = cv2.rectangle(Task_1_insights, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)

        xs = str(x_start)
        xe = str(x_end)
        ys = str(y_start)
        ye = str(y_end)
        x = f"({xs}, {ys})"
        y = f"({xe}, {ye})"
        Task_1_insights = cv2.putText(Task_1_insights, x, (x_start, y_start), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        Task_1_insights = cv2.putText(Task_1_insights, y, (x_end, y_end), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow("Task_1_insights", Task_1_insights)
        cv2.imwrite('task-1-insights.jpg', Task_1_insights)

    cv2.waitKey(1)


