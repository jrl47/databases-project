/**
 * The object used to manage the view of the website.
 */
function View(data) {
    View.self = this;
    this.root = document.getElementById('react-container');
    // ReactDOM.render(React.createElement(Board,
    //     {board: this.data.getBoardData(), modelCallback: this.modelCallback}),
    //     this.root);
    this.update(false);
}

/**
 * The method used to re-render the View based on the value of this.data.
 */
View.prototype.update = function(newCase) {
    ReactDOM.render(React.createElement(ModuleContainer,
        {case: newCase}),
        this.root);
};

/**
 * The master React component containing all subcomponents.
 */
ModuleContainer = function(props) {
    return React.createElement(Title,
        {case: props.case});
};

ModuleContainer.propTypes = {
    case: React.PropTypes.bool.isRequired,
}

/**
 * An interactive Title module for test purposes.
 */
Title = function(props) {
    var title = 'databases';
    if(props.case) {
        title = 'DATABASES';
    }
    return React.createElement('h1',
        {onClick: function changeCase() {
            View.prototype.update.apply(View.self, [!props.case])},
        style: {textAlign:'center', padding: '0px'}},
        title);
};

Title.propTypes = {
    case: React.PropTypes.bool.isRequired,
}