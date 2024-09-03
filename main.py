import cv2
from ultralytics import YOLO

def run_detection(source, model_path='best.pt'):
    model = YOLO(model_path)

    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()
        print(f"Frame read successful: {success}")

        if success:
            # Running YOLOv8 inference on the frame
            results = model(frame)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # if end of the video
            break

    # close window
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Choose between webcam and video file
    use_webcam = False  # Set to True to use webcam

    if use_webcam:
        source = 0
    else:
        source = "data/test_video.mp4"

    run_detection(source, model_path="models/best.pt")
