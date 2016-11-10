Board = function(props) {
    return React.createElement('table', {style: {borderCollapse: 'collapse'}},
        React.createElement(BoardBody, props));
};

Board.propTypes = {
    board: React.PropTypes.instanceOf(GameData.BoardData).isRequired,
    modelCallback: React.PropTypes.func.isRequired
}

BoardBody = function(props) {
    var rows = [];
    for (var i = 0; i < props.board.getSize(); i++) {
        var childProps = {row: props.board.getRow(i), y: i, modelCallback: props.modelCallback};
        rows[i] = React.createElement(BoardRow, childProps);
    }
    return React.createElement.apply(this, ['tbody', props].concat(rows));
};

BoardBody.propTypes = {
    board: React.PropTypes.instanceOf(GameData.BoardData).isRequired,
    modelCallback: React.PropTypes.func.isRequired
}

BoardRow = function(props) {
    var cells = [];
    for (var i = 0; i < props.row.length; i++) {
        var childProps = {cell: props.row[i], y: props.y, x: i, modelCallback: props.modelCallback};
        cells[i] = React.createElement(BoardCell, childProps);
    }
    return React.createElement.apply(this, ['tr', props].concat(cells));
};

BoardRow.propTypes = {
    row: React.PropTypes.arrayOf(GameData.BoardData.LocationData).isRequired,
    modelCallback: React.PropTypes.func.isRequired
}

BoardCell = function(props) {
    return React.createElement('td',
        {onClick: function place() {props.modelCallback.apply(this, [new Action('place',
        {x: props.x, y: props.y})])},
        style: {border: '1px solid #000000', textAlign:'center',
        padding: '0px', width:20, height:20}},
        View.getCellSymbol(props.cell));
};

BoardCell.propTypes = {
    cell: React.PropTypes.instanceOf(GameData.BoardData.LocationData).isRequired,
    modelCallback: React.PropTypes.func.isRequired
}

/**
 * The method used to select what to display for a given LocationData.
 */
View.getCellSymbol = function(cell) {
    if (!cell.hasBlackPiece && !cell.hasWhitePiece &&
        !cell.hasBlackMark && !cell.hasWhiteMark) {
        return ' ';
    } else if (cell.hasBlackPiece && !cell.hasWhitePiece) {
        return 'B';
    } else if (!cell.hasBlackPiece && cell.hasWhitePiece) {
        return 'W';
    } else if (cell.hasBlackPiece && cell.hasWhitePiece) {
        return 'X'
    } else if (cell.hasBlackMark && !cell.hasWhiteMark) {
        return 'b';
    } else if (!cell.hasBlackMark && cell.hasWhiteMark) {
        return 'w';
    } else {
        return 'x';
    }
};