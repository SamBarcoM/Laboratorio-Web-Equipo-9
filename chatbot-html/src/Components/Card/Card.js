import React from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import './Card.css';

class Card extends React.Component {
	render() {
		return (
			<div className="card">
				<div className="card__header">
					{this.props.icon ? <FontAwesomeIcon icon={this.props.icon} size="4x" color={this.props.iconColor} /> : null}
					<div>
						<h4 className="card__header__title">{this.props.title}</h4>
						<p className="card__header__description">{this.props.description}</p>
					</div>
				</div>
				<div className="card_content">
					{this.props.children}
				</div>
			</div>
		);
	}
}
export default Card;
