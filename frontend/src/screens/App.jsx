import React, { Component } from 'react';
import '../css/App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      item : "",
      days: 0
    }
  }

  onChangeItem(event) {
    this.setState({
      item: event.target.value
    })
  }

  onChangeDays(event) {
    this.setState({
      days: event.target.value
    })
  }

  getItems(item, days) {
    alert(item + " needs to be shipped within " + days + " days.");
  }

  render() {
    return (
      <div className="app">
        <p className="title">Ship-It</p>
        <div className="form">
          <input
            className="input item-input"
            placeholder="Ex: Toilet Paper, Snacks, Toothbrush"
            onChange={event => this.onChangeItem(event)}  
          />
          <input
            className="input date-input"
            placeholder="Days for shipping"
            onChange={event => this.onChangeDays(event)}
          />
          <button
            className="btn btn-light btn-submit"
            onClick={() => this.getItems(this.state.item, this.state.days)}
          >
              Find Items
          </button>
        </div>
      </div>
    );
  }  
}

export default App;
