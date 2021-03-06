import React, { Component } from 'react';
import '../css/App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import ItemCard from '../components/ItemCard';
import Loader from 'react-loader-spinner';

class App extends Component {

  constructor(props) {
    super(props);
    
    this.state = {
      item : "",
      days: 0,
      items: [],
      loading: false
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
    this.setState({ loading: true }, () => {
      fetch(
        `http://localhost:5000/api/item?item=${item}&days=${days}`
      ).then(res => {
        return res.json();
      }).then(data => {
        console.log(data);
        this.setState({
          loading: false,
          items: data
        })
      });
    });
  }

  render() {
    return (
      <div className="app">
        <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro&display=swap" rel="stylesheet"></link>
        <p className="title">Ship It</p>
        <p className="info">Get all your essentials exactly when you want them</p>
        <div className="form">
          I want . . .
          <input
            className="input item-input"
            placeholder="toilet paper, snacks, toothbrush"
            onChange={event => this.onChangeItem(event)}  
          /> within
          <input
            className="input date-input"
            placeholder="5"
            onChange={event => this.onChangeDays(event)}
          /> days.
          <button
            className="btn btn-light btn-submit"
            onClick={() => this.getItems(this.state.item, this.state.days)}
          >
              Search
          </button>
        </div>
        
        {this.state.loading ? <Loader type="ThreeDots" color="#ae621f"/> : (
          <div className="items">
            {this.state.items.map((item, i) => <ItemCard item={item} key={i} number={i}/>)}
          </div>
        )}
      </div>
    );
  }  
}

export default App;
