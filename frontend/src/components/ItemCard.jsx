import React, { Component } from 'react'
import '../css/ItemCard.css'

export default class ItemCard extends Component {

  orderItem() {
    window.open("https://google.com/search?q=" + this.props.item.store_name + " "+ this.props.item.item_name);
  }

  render() {
    return (
      <div className="card">
        <div className="card-title">
          {this.props.number + 1}. {this.props.item.item_name}
        </div>
        <img className="item-image" src={this.props.item.image} width="150px" height="150px"></img>
        <div className="card-store">
          {this.props.item.store_name}
        </div>
        <div className="card-price">
          <span className="money"> ${this.props.item.initial_price} </span> initial price
        </div>
        <div className="card-price">
          <span className="money"> ${this.props.item.total_price} </span> plus tax with shipping within {this.props.item.shipping_days} days
        </div>
        <button onClick={() => this.orderItem()} className="btn btn-success btn-order">
          Order Item
        </button>
      </div>
    )
  }
}
