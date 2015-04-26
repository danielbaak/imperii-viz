//
//  TimeLineView.swift
//  ImperiiViz
//
//  Created by Frederik Riedel on 26.04.15.
//  Copyright (c) 2015 Frederik Riedel. All rights reserved.
//

import UIKit

protocol TimeLineViewDelegate {
    func yearChanged(year: Float)
}



class TimeLineView: UIView {
   
    var from : NSDateComponents
    var to : NSDateComponents
    var delegate : TimeLineViewDelegate?
    
    init(frame: CGRect, from: NSDateComponents, to: NSDateComponents) {
        self.from = from
        self.to = to
        
        super.init(frame: frame)
        
        

        var numberOfYearsInRow = 7
        var widthOfYearLabel = self.frame.size.width / CGFloat(numberOfYearsInRow+1)
        
        for var i = 0; i <= numberOfYearsInRow; i++ {
            var yearLabel = UILabel(frame: CGRectMake(widthOfYearLabel * CGFloat(i), 0, CGFloat(widthOfYearLabel), self.frame.height))
            
            var roundedYear = from.year + Int(Float(Float(i)/Float(numberOfYearsInRow)) * Float(to.year-from.year))
            
            yearLabel.text=String(roundedYear)
            println(String(roundedYear))
            
            yearLabel.textAlignment=NSTextAlignment.Center
            self.addSubview(yearLabel)
        }
        
    }

    required init(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    
    override func touchesMoved(touches: Set<NSObject>, withEvent event: UIEvent) {
        let touchCount = touches.count
        let touch = touches.first as! UITouch
        let tapCount = touch.tapCount
        
        var slectedYear = CGFloat(from.year) + (CGFloat(touch.locationInView(self).x) / self.frame.width) * CGFloat(to.year - from.year)
        
        delegate?.yearChanged(Float(slectedYear))
    }
    
    
}
