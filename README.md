# 2D GUI using Pyqt5

This README.md will explain the implementation code for the 2021 NHIS 2D GUI created using Pyqt5. There are a total of 6 Python files.

Before using this GUI it is important to make sure you have the Pyqt5 package installed to your computer. To do so, you may type in the command: py -m pip install pyqt5, into your terminal. 

To load the GUI you may open a terminal on your computer and type: py pip path-to-NHIS2021_2D_GUI-folder/Main.py. Alternatively, you may load the Python classes from the NHIS2021_2D_GUI folder in this GitHub repository into a code editor, such as VSCode, and run the Main.py class from there.

## ChiSquare2Var.py

We import necessary modules from the Pyqt5 library: QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox, QLineEdit, Qt, and QFont

### class ChiSquare2Var(QWidget):

*ChiSquare2Var()* passes in QWidget which is a base class for all GUI objects in Pyqt5. It provides functions like creating a window where you can place buttons, labels, text, and other Pyqt5 supported elements.

- ***def __init__(self, data)***:
In our constructor, we create class attributes called *data* and *labels*. The attribute called *data* represents the dataset of our chi-square test csv file while *labels* represents a dictionary of labels which will eventually hold the columns *dep_x_squared*, *dep_p_value*, *anx_x_squared*, and *anx_p_value* from our chi.csv file. We then set the window flags to stay on top in order to ensure that when we're clicking around in the main menu, our ChiSquare2Var window doesn't get pushed behind. Lastly, we initialize the user interface.

- ***def init_ui(self)***:
In our *init_ui()* method we begin to initialize the components within the user interface. First, we declare a vertical layout which arranges the GUI elements vertically. Next, we create the label for our search box with a font of size 14. Inside of the search box, we place the defaulted text to "Enter specific format" to remind the user that they must enter the specific format as seen from the chi-csv file. This is also set to a font size of 14. Next we connect the searched text signal to the update_combo_box() method. This will essentially match the input from the search box to the items in the drop down box. Then, we add the created labels as a widget to the GUI layout. Next, we create a label for the text "or" which will indicate to the user that there is an alternative way of selecting a question combination. This label is aligned to be centered with a font size of 14, and then it is added as a widget to the GUI layout. Next, we create and add the label "Select the question combination:" and a drop down box as a widget on the GUI layout. By doing so, it allows the user to scroll through and select a question combination. These are both set to a font size of 14. Lastly we create a button that says "Submit" on it with a font size of 14 which calls the calculate_chi_square() method when clicked on. Next we create a label to display the results obtained from the calculate_chi_square() method with a font size of 14 and add it as a widget to the GUI layout. Then in order to ensure that our GUI elements that we have previously created and added are arranged in an organized manner we set the layout for all the widgets using the .setLayout() method. Next, we add in the options for our drop down box. Lastly, we set the window title to *ChiSquare2Var* and the width of the window to 450 pixels. 

- ***def update_combo_box(self, text)***:
This method updates the option selected in the drop down box according to the text entered in the search box. 

- ***def calculate_chi_square(self)***:
Our *calculate_chi_square()* method we check if the question combintation exists in the index of the dataset. If it does exist in the dataset, we locate the row corresponding to this question combination. Next we create an empty String which we will use to store our final formatted result. We iterate through the dictionary which contains the labels for *dep_x_squared*, *dep_p_value*, *anx_x_squared*, and *anx_p_value*. For each label in the dictionary, it gets their respective values from the row we decected earlier using the column names. It then appends the formatted text of label + value to the empty String we created. Then we set the text from our appended String as a widget for the selected question combination on the GUI layout. If the question combination does not exist in the dataset, a warning message box is displayed.

## DataSet.py

We import necessary libraries from Pandas 

### class DataSet:

- ***def load_data(dataset_url, index_col=None):***
We have a static method called *load_data()* which allows us to call this method from ourside of the class without having to create an instance of the DataSet class. This method uses the Pandas library to read in a csv file from a designated url address. It then returns the loaded data.

## Main.py

We import necessary modules: sys, QApplication, DataSet, and MainMenu.

- ***def __init__(self, dataset_url, chi_dataset_url):***
Our constructor for the *Main()* class takes in  two parameters, one for the cleaned 2021 NHIS dataset and one for the chi-square test dataset.  These parameters are initalized here.

- ***def load_data(self):***
This method uses the *load_data()* method from the DataSet class to load in the datasets and set them to our *data* and *chi_data* iknstance variables.

- ***def run(self):***
The *load_data()* is called first, and then an instance of the MainMenu class is created. This instance is then shown as a window, and an application event loop is started.

### if __name__ == "__main__":
This checks if the script is being run as the main module. If it is, we define the url addresses for the datasets and create an instance of the *Main()* class using these datasets. We then call the *run()* method onto the instance we created to start the execution of the GUI application.

## MainMenu.py

We import necessary modules from Pyqt5: QMainWindow, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, Qt, and QFont. We also import the modules: ChiSquare2Var, DataSet, ThreeDGraph, and TwoDGraph.

### class MainMenu(QMainWindow):
*MainMenu()* passes in QMainWindow which represents the main menu window of this GUI application. By doing so, we are making the *MainMenu()* class to become the main interface of this GUI application that can contain other widgets.

- ***def __init__(self, data, chi_data):***
This is our constructor method for our *MainMenu()* class. We initialize the main menu window, and the instance variables (*data*, *chi_data*, and *chi_widget*) of our class.

- ***def init_ui(self):***
In this method we essentially initalize the user interface of the main menu window. First we set the window title to "2021 National Health Interview Survey (NHIS) 2D GUI" and resize the window to be 1900 by 1000. Next we create the title label for our main menu window and align it to be centered. Next we set the font size to 28, the color to hex #252547, and bold it. Then we create a layout instance which sets the layout of the main menu window to verticle. We then align the widgets to the top of the main menu window. Then the title label is added as a widget to the layout. Next, we create a spacer to create some space in between the title label and the buttons that we want to create in the main menu window. Now, we create a layout instance of horizontal and align it to be centered. This will allow us to but all of our buttons next to each other instead of being stacked on top of each other. Next, we declare the specific color hex numbers we want our *3D Graph* and *Chi-Square Analysis (2 Variables)* buttons to be. and declare a font size of 14. We then create a push button that connects the button clicking event to the *show_2d_graph()* method. We set the size of the button to be 450 by 40 pixels with a font size of 14 and a font style of Arial. Then we add the button to the layout. We repeat the same steps for our *3D Graph* button except we call the *show_3d_graph()* method when the button is clicked. Likewise, we repeat the same steps for our *Chi-Square Analysis (2 Variables)* button except we call the *show_chi_square()* method when the button is clicked. Now we add the button layout to the main layout of the main menu window. This ensures that the buttons are placed under the title label. Then, we change the background color of the window to hex #CCCCCC.

- ***def show_2d_graph(self):***
An instance of the *TwoDGraph()* class is created here which is then shown to the main menu window using the *.show()* function. This generates a 2D plot.

- ***def show_3d_graph(self):***
An instance of the *ThreeDGraph()* class is created here which is then shown to the main menu window using the *.show()* function. This generates a 3D plot.

- ***def show_chi_square(self):***
This method first checks if the chi-square test window has not been created. If it hasn't, an instance of the *ChiSquareVar2()* class is created. Then it is shown to the main menu window using the *.show()* function. This ensures that a chi-square test window is created and generated.
